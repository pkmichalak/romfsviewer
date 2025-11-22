import sys
import struct
import binascii
from io import BufferedReader
from enum import Enum
from dataclasses import dataclass

@dataclass
class RomFsHdr:
	hdr1        : bytes
	hdr2        : bytes
	full_size   : int
	checksum    : int
	volume_name : str
	def next(self) -> int:
		return 4 + 4 + 4 + 4 + len(self.volume_name)
	def volume_name_desc(self) -> str:
		return self.volume_name.decode("utf-8", errors="replace")

@dataclass
class RomFsFileHdr:
	next_file_hdr : int
	spec_info     : int
	size          : int
	checksum      : int
	file_name     : str
	file_data     : bytes
	OFFSET_MASK      = 0xFFFFFFF0
	TYPE_MASK        = 0x00000003
	EXECUTABLE_MASK  = 0x00000008
	EXECUTABLE_SHIFT = 3
	def next(self) -> int:
		return self.next_file_hdr & self.OFFSET_MASK
	def file_type(self) -> int:
		return self.next_file_hdr & self.TYPE_MASK
	def file_type_desc(self) -> int:
		return "{} ({})".format(self.file_type(), RomFsFileType(self.file_type()).name)
	def file_executable(self) -> bool:
		return 1 == ((self.next_file_hdr & self.EXECUTABLE_MASK) >> self.EXECUTABLE_SHIFT)
	def file_name_desc(self) -> str:
		return self.file_name.decode("utf-8", errors="replace")
	def file_data_desc(self, size: int=16) -> str:
		data = self.file_data[0:size]
		try:
			return data.decode("utf-8").replace('\n', '\\n').replace('\t', '\\t').replace('\r', '\\r')
		except Exception as E:
			return "0x" + data.hex()
	def file_data_offset(self) -> int:
		return 4 + 4 + 4 + 4 + len(self.file_name)


class RomFsFileType(Enum):
	HARD_LINK = 0
	DIRECTORY = 1
	REGULAR_FILE = 2
	SYMBOLIC_LINK = 3
	BLOCK_DEVICE = 4
	CHAR_DEVICE = 5
	SOCKET = 6
	FIFO = 7


def read_zero_terminated_boundary(file, boundary: int) -> bytes:
	b = file.read(boundary)
	b_all = b
	while b[15] != 0x00:
		b = file.read(boundary)
		b_all = b_all + b

	return b_all


def romfs_print_legend():
	print("{:20}   {:10}   {:10}   {:10}  {}"      .format("field",  "size", "start", "end",  "value"))
	print("{:20}   {:10}   {:10}   {:10}  {}"      .format("-"*20,  "-"*10, "-"*10, "-"*10,  "-"*30))

def romfs_print_bar():
	print("{:20}   {:10}   {:10}   {:10}  {}"      .format("-"*20,  "-"*10, "-"*10, "-"*10,  "-"*30))

def romfs_print_line_std(field: str, size: int, start: int, value):
	print("{:20}  ({:10}) [{:10} - {:10}] {}"      .format(field, size, start, start + size - 1, value))

def romfs_print_line_hex(field: str, size: int, start: int, value):
	print("{:20}  ({:10}) [{:10} - {:10}] 0x{:08x}".format(field, size, start, start + size - 1, value))


def romfs_print_hdr(hdr: RomFsHdr, offset: int) -> int:
	o = offset
	s = 4;
	romfs_print_line_std("hdr1",               s, o, hdr.hdr1);                  o += s
	romfs_print_line_std("hdr2",               s, o, hdr.hdr2);                  o += s
	romfs_print_line_std("full size",          s, o, hdr.full_size);             o += s
	romfs_print_line_hex("checksum",           s, o, hdr.checksum);              o += s
	s = len(hdr.volume_name)
	romfs_print_line_std("volume name",        s, o, hdr.volume_name_desc());    o += s
	return o


def romfs_print_file_hdr(file_hdr: RomFsFileHdr, offset: int) -> int:
	o = offset
	s = 4
	romfs_print_line_std("next file hdr",      s, o, file_hdr.next_file_hdr);
	romfs_print_line_std(" | next",            s, o, file_hdr.next());
	romfs_print_line_std(" | file type",       s, o, file_hdr.file_type_desc());
	romfs_print_line_std(" | file executable", s, o, file_hdr.file_executable());

	o += s
	romfs_print_line_std("spec_info",          s, o, file_hdr.spec_info);        o += s
	romfs_print_line_std("size",               s, o, file_hdr.size);             o += s
	romfs_print_line_hex("checksum",           s, o, file_hdr.checksum);         o += s
	s = len(file_hdr.file_name)
	romfs_print_line_std("file name",          s, o, file_hdr.file_name_desc()); o += s
	if 0 < file_hdr.size:
		s = file_hdr.size
		romfs_print_line_std("file data",        s, o, file_hdr.file_data_desc()); o += s
	return o


def romfs_view_file(f: BufferedReader, next: int):

	while (0 != next):

		f.seek(next)
		file_hdr = RomFsFileHdr(
			struct.unpack('>I', f.read(4))[0],
			struct.unpack('>I', f.read(4))[0],
			struct.unpack('>I', f.read(4))[0],
			struct.unpack('>I', f.read(4))[0],
			read_zero_terminated_boundary(f, 16),
			None
		)
		if 0 < file_hdr.size:
			file_hdr.file_data = f.read(file_hdr.size)

		romfs_print_bar()
		romfs_print_file_hdr(file_hdr, next)

		if RomFsFileType.DIRECTORY.value == file_hdr.file_type() \
			and 32 < file_hdr.spec_info:
			romfs_view_file(f, file_hdr.spec_info)

		next = file_hdr.next()


def romfs_view(romfs_filename: str):

	with open(romfs_filename, "rb") as romfs_image:
		f = romfs_image
		hdr = RomFsHdr(
			f.read(4),
			f.read(4),
			struct.unpack('>I', f.read(4))[0],
			struct.unpack('>I', f.read(4))[0],
			read_zero_terminated_boundary(f, 16)
		)

		romfs_print_legend()
		o = 0
		o = romfs_print_hdr(hdr, o)

		romfs_view_file(f, hdr.next())


if __name__ == "__main__":

	if 2 != len(sys.argv):
		print("no filename specified")
		exit(1)

	arg1 = sys.argv[1]
	romfs_view(arg1)
