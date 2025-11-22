# romfsviewer

Simple ROMFS filesystem image examination tool in python3


Usage:

python3 romfsviewer.py image.romfs


Links:

https://en.wikipedia.org/wiki/Romfs

https://docs.kernel.org/filesystems/romfs.html


Test image create with:

genromfs -f image.romfs -d data


Example:

python3 src/romfsviewer.py data-test/image.romfs


field                  size         start        end         value
--------------------   ----------   ----------   ----------  ------------------------------
hdr1                  (         4) [         0 -          3] b'-rom'
hdr2                  (         4) [         4 -          7] b'1fs-'
full size             (         4) [         8 -         11] 2849744
checksum              (         4) [        12 -         15] 0x3f43d5b4
volume name           (        16) [        16 -         31] rom 69222ddd
--------------------   ----------   ----------   ----------  ------------------------------
next file hdr         (         4) [        32 -         35] 73
 | next               (         4) [        32 -         35] 64
 | file type          (         4) [        32 -         35] 1 (DIRECTORY)
 | file executable    (         4) [        32 -         35] True
spec_info             (         4) [        36 -         39] 32
size                  (         4) [        40 -         43] 0
checksum              (         4) [        44 -         47] 0xd1ffff97
file name             (        16) [        48 -         63] .
--------------------   ----------   ----------   ----------  ------------------------------
next file hdr         (         4) [        64 -         67] 96
 | next               (         4) [        64 -         67] 96
 | file type          (         4) [        64 -         67] 0 (HARD_LINK)
 | file executable    (         4) [        64 -         67] False
spec_info             (         4) [        68 -         71] 32
size                  (         4) [        72 -         75] 0
checksum              (         4) [        76 -         79] 0xd1d1ff80
file name             (        16) [        80 -         95] ..
--------------------   ----------   ----------   ----------  ------------------------------
next file hdr         (         4) [        96 -         99] 85362
 | next               (         4) [        96 -         99] 85360
 | file type          (         4) [        96 -         99] 2 (REGULAR_FILE)
 | file executable    (         4) [        96 -         99] False
spec_info             (         4) [       100 -        103] 0
size                  (         4) [       104 -        107] 85218
checksum              (         4) [       108 -        111] 0x6f1d95d1
file name             (        16) [       112 -        127] boat.png
file data             (     85218) [       128 -      85345] 0x89504e470d0a1a0a0000000d49484452
--------------------   ----------   ----------   ----------  ------------------------------
next file hdr         (         4) [     85360 -      85363] 213081
 | next               (         4) [     85360 -      85363] 213072
 | file type          (         4) [     85360 -      85363] 1 (DIRECTORY)
 | file executable    (         4) [     85360 -      85363] True
spec_info             (         4) [     85364 -      85367] 85392
size                  (         4) [     85368 -      85371] 0
checksum              (         4) [     85372 -      85375] 0xbc219e92
file name             (        16) [     85376 -      85391] jpg files
--------------------   ----------   ----------   ----------  ------------------------------
next file hdr         (         4) [     85392 -      85395] 213010
 | next               (         4) [     85392 -      85395] 213008
 | file type          (         4) [     85392 -      85395] 2 (REGULAR_FILE)
 | file executable    (         4) [     85392 -      85395] False
spec_info             (         4) [     85396 -      85399] 0
size                  (         4) [     85400 -      85403] 127581
checksum              (         4) [     85404 -      85407] 0x54180563
file name             (        16) [     85408 -      85423] Ara.jpg
file data             (    127581) [     85424 -     213004] 0xffd8ffdb004300040303040303040403
--------------------   ----------   ----------   ----------  ------------------------------
next file hdr         (         4) [    213008 -     213011] 213040
 | next               (         4) [    213008 -     213011] 213040
 | file type          (         4) [    213008 -     213011] 0 (HARD_LINK)
 | file executable    (         4) [    213008 -     213011] False
spec_info             (         4) [    213012 -     213015] 32
size                  (         4) [    213016 -     213019] 0
checksum              (         4) [    213020 -     213023] 0xd1cebfb0
file name             (        16) [    213024 -     213039] ..
--------------------   ----------   ----------   ----------  ------------------------------
next file hdr         (         4) [    213040 -     213043] 0
 | next               (         4) [    213040 -     213043] 0
 | file type          (         4) [    213040 -     213043] 0 (HARD_LINK)
 | file executable    (         4) [    213040 -     213043] False
spec_info             (         4) [    213044 -     213047] 85360
size                  (         4) [    213048 -     213051] 0
checksum              (         4) [    213052 -     213055] 0xd1feb290
file name             (        16) [    213056 -     213071] .
--------------------   ----------   ----------   ----------  ------------------------------
next file hdr         (         4) [    213072 -     213075] 2814681
 | next               (         4) [    213072 -     213075] 2814672
 | file type          (         4) [    213072 -     213075] 1 (DIRECTORY)
 | file executable    (         4) [    213072 -     213075] True
spec_info             (         4) [    213076 -     213079] 213104
size                  (         4) [    213080 -     213083] 0
checksum              (         4) [    213084 -     213087] 0xb5f9f932
file name             (        16) [    213088 -     213103] png files
--------------------   ----------   ----------   ----------  ------------------------------
next file hdr         (         4) [    213104 -     213107] 686994
 | next               (         4) [    213104 -     213107] 686992
 | file type          (         4) [    213104 -     213107] 2 (REGULAR_FILE)
 | file executable    (         4) [    213104 -     213107] False
spec_info             (         4) [    213108 -     213111] 0
size                  (         4) [    213112 -     213115] 473831
checksum              (         4) [    213116 -     213119] 0x42e3317f
file name             (        32) [    213120 -     213151] Lenna_test_image.png
file data             (    473831) [    213152 -     686982] 0x89504e470d0a1a0a0000000d49484452
--------------------   ----------   ----------   ----------  ------------------------------
next file hdr         (         4) [    686992 -     686995] 2163426
 | next               (         4) [    686992 -     686995] 2163424
 | file type          (         4) [    686992 -     686995] 2 (REGULAR_FILE)
 | file executable    (         4) [    686992 -     686995] False
spec_info             (         4) [    686996 -     686999] 0
size                  (         4) [    687000 -     687003] 1476396
checksum              (         4) [    687004 -     687007] 0xd07f2c5b
file name             (        16) [    687008 -     687023] Jupiter.png
file data             (   1476396) [    687024 -    2163419] 0x89504e470d0a1a0a0000000d49484452
--------------------   ----------   ----------   ----------  ------------------------------
next file hdr         (         4) [   2163424 -    2163427] 2163456
 | next               (         4) [   2163424 -    2163427] 2163456
 | file type          (         4) [   2163424 -    2163427] 0 (HARD_LINK)
 | file executable    (         4) [   2163424 -    2163427] False
spec_info             (         4) [   2163428 -    2163431] 32
size                  (         4) [   2163432 -    2163435] 0
checksum              (         4) [   2163436 -    2163439] 0xd1b0fce0
file name             (        16) [   2163440 -    2163455] ..
--------------------   ----------   ----------   ----------  ------------------------------
next file hdr         (         4) [   2163456 -    2163459] 2814642
 | next               (         4) [   2163456 -    2163459] 2814640
 | file type          (         4) [   2163456 -    2163459] 2 (REGULAR_FILE)
 | file executable    (         4) [   2163456 -    2163459] False
spec_info             (         4) [   2163460 -    2163463] 0
size                  (         4) [   2163464 -    2163467] 651142
checksum              (         4) [   2163468 -    2163471] 0xbf948ce9
file name             (        16) [   2163472 -    2163487] baboon.png
file data             (    651142) [   2163488 -    2814629] 0x89504e470d0a1a0a0000000d49484452
--------------------   ----------   ----------   ----------  ------------------------------
next file hdr         (         4) [   2814640 -    2814643] 0
 | next               (         4) [   2814640 -    2814643] 0
 | file type          (         4) [   2814640 -    2814643] 0 (HARD_LINK)
 | file executable    (         4) [   2814640 -    2814643] False
spec_info             (         4) [   2814644 -    2814647] 213072
size                  (         4) [   2814648 -    2814651] 0
checksum              (         4) [   2814652 -    2814655] 0xd1fcbfb0
file name             (        16) [   2814656 -    2814671] .
--------------------   ----------   ----------   ----------  ------------------------------
next file hdr         (         4) [   2814672 -    2814675] 2814722
 | next               (         4) [   2814672 -    2814675] 2814720
 | file type          (         4) [   2814672 -    2814675] 2 (REGULAR_FILE)
 | file executable    (         4) [   2814672 -    2814675] False
spec_info             (         4) [   2814676 -    2814679] 0
size                  (         4) [   2814680 -    2814683] 15
checksum              (         4) [   2814684 -    2814687] 0xf691afa2
file name             (        16) [   2814688 -    2814703] textfile.txt
file data             (        15) [   2814704 -    2814718] line 1\n\tline 2\n
--------------------   ----------   ----------   ----------  ------------------------------
next file hdr         (         4) [   2814720 -    2814723] 2
 | next               (         4) [   2814720 -    2814723] 0
 | file type          (         4) [   2814720 -    2814723] 2 (REGULAR_FILE)
 | file executable    (         4) [   2814720 -    2814723] False
spec_info             (         4) [   2814724 -    2814727] 0
size                  (         4) [   2814728 -    2814731] 34975
checksum              (         4) [   2814732 -    2814735] 0x5f4913e1
file name             (        32) [   2814736 -    2814767] This is a A4 Test Document.pdf
file data             (     34975) [   2814768 -    2849742] 0x255044462d312e350d25e2e3cfd30d0a


