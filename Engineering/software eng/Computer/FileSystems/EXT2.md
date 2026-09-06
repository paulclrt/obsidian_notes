
This dates back to the origins of linux.
in 1991, Linux had one filesystem availabel based on minix (minixFS --> Simple so stable).
in 1992, there was a push for newer files sytems. So Linux (community) built the VFS (virtual filesystem).
This is an abstraction from the on disk FS so apps talk only to VFS and you can have any filesytem underneeth.

So Rémy card created the first ext (extended file system): ext 

Limitations of Minix:

|               | Mimix   | EXT       | XiaFS     | EXT2      |
| ------------- | ------- | --------- | --------- | --------- |
| FS Size       | 64MB    | 2GB       | 2GB       | 4TB       |
| File Size     | 64MB    | 2GB       | 64MB      | 2GB       |
| File Name<br> | 16chars | 255 chars | 248 chars | 255 chars |

But the implementation wasn't stable... so they created XiaFS (minix but bigger)
The ext familly of FS is extenable and is built from the previous ext.

## How it is actually built

Concepts:
*inode:* pointer to data (location on drive); time modified; permissions
*block:* the hard drive is a division of the drive blocks are supposed to be the same size of your system page size

here is a 20mb partition with 1Kb block:
![[20mb_drive_ext2.png]]

The first block (before 0) is just the MBR...
In EXT everything is splitted into block groups.

The first two block groups have a **superblock** and a **descriptior table**. In later revision these are not present in every block groups

### Superblocks
Here is a superblock:
![[superblock_ext2.png|380]]

The superblock is information for when you are mounting the drivre. (should we check this block for errors ? what os is used with this FS ? ...)
In green there is the reserve for upgrade (hehe)

### Descriptor tables

Now you know how to mount the drive wit hthe superblock. But how do you read the data ?
You look this up
![[group_descriptor_table_ext2.png|742]]
This is one entry in the table. 
This tells you where is the 
- block bitmap
- inode bitmap
- the inode table
- freespace available in this block ? (free blocks count, inodes count)
- again here reserved spaced

### Block and inode bitmap
![[block_inode_bitmaps.png|282]]

Bitmap: 1 = block used, 0 = freespace there

### Inode table
![[inode_table_ext2.png|450]]

The inode table is a big table that contains all the inodes.

*i_mode*: what is at the end of this inode (dir, file, drive... )
*i_size*: size of the data
*i_atime*: access time
*i_ctime*: creation time
*i_mtime*: modifictaion time
*i_dtime*: deletion time
*uig, gid*: 
*links_count*: an inode can be linked by multiple directory (sym linsk, hardlinks  etc ???)
*i_block*: this is the juicy stuff

### I_block
![[i_block_ext2.png|526]]

*Direct block pointer*: directly points to a block full of data
*Indirect block pointer*: pointing to another similar i_block structure (without the other indirect)
*Doubly-indirect*: The same as indirect block pointer but deeper (see second image below)
*Triply-indirect*;


![[indirect_block_pointers_ext2.png|695]]
Here again the double
![[doubly_indirect_blockpointer_ext2.png|750]]


## Directories

![[directory_ext2.png|798]]
Before, we were storing but didn't have names etc.
Here we have an entry of a directory where you have the inode (location on disk remember?), rec_lend, name_len (and a name of max 255 chars)


## Seeing it in action

Running LS, here is what comes up:
![[directory_table_example_ext2.png|680]]
Entry one is the .. which is parent dir. for a .bash_profile file name you would see name=.bash_profile and name_len=13