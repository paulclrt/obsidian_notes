Source: https://www.youtube.com/watch?v=Fq0ks85G6-o&list=PLkoRSCZZILDPJE0iMlTatTBBgHxcnek4R&index=2

For every program to work on different filesystems you go throught he kernel and use VFS.
![[call_structure_vfs_early.png|791]]
Here is a modern version
![[call_structure_vfs_modern.png|789]]

There are now caches that were added.

| Name | Parent pointer | Inode pointer |
| ---- | -------------- | ------------- |
| a    | NULL           | 0011          |
| b    | NULL           | 0012          |
| c    | NULL           | 0002          |
| 1    | 0001           | 0003          |
| 2    | 0002           | 0004          |
| 3    | 0003           | 0005          |
It works like this
![[cache_entries_vfs.png|703]]
When you boot it starts to construct this cache. This is a very nice optimisation for performance.


### How programs get to open the files

Process ask for a file descriptor (process version of a file),
From VFS pov this is a file object which points to dentry cache (directory entry cache)
It finds an entry that matches then goes to inode (if symlink to follows it)

![[cache_path.png]] This is the path we follow in vfs to find the file.

Then it goes to the ext callbacks...