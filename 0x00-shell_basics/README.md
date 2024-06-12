# 0x00-shell_basics

This project, `0x00-shell_basics`, is part of my journey through the ALX program, focusing on learning basic shell commands and scripting. The project consists of several tasks, each represented by a file. Some tasks are mandatory, while others are advanced.

## Table of Contents

- [Introduction](#introduction)
- [Project Structure](#project-structure)
- [Mandatory Tasks](#mandatory-tasks)
- [Advanced Tasks](#advanced-tasks)
- [Contact](#contact)

## Introduction

The `0x00-shell_basics` project aims to introduce fundamental shell commands and scripting techniques. Each task in this project is designed to teach a specific concept or command, providing a solid foundation in shell scripting.

## Project Structure

The project is organized into tasks, each with its own file. The tasks are divided into mandatory and advanced categories.

## Mandatory Tasks

1. **0. Where am I?**
   - **File:** `0-current_working_directory`
   - **Description:** Write a script that prints the absolute path name of the current working directory.
   - **Example:**
     ```sh
     $ ./0-current_working_directory
     /root/alx-system_engineering-devops/0x00-shell_basics
     ```

2. **1. What’s in there?**
   - **File:** `1-listit`
   - **Description:** Display the contents list of your current directory.
   - **Example:**
     ```sh
     $ ./1-listit
     Applications    Documents    Dropbox  Movies  Pictures
     Desktop         Downloads    Library  Music   Public
     ```

3. **2. There is no place like home**
   - **File:** `2-bring_me_home`
   - **Description:** Write a script that changes the working directory to the user’s home directory.
   - **Example:**
     ```sh
     julien@ubuntu:/tmp$ source ./2-bring_me_home
     julien@ubuntu:~$ pwd
     /home/julien
     ```

4. **3. The long format**
   - **File:** `3-listfiles`
   - **Description:** Display current directory contents in a long format.
   - **Example:**
     ```sh
     $ ./3-listfiles
     total 32
     -rwxr-xr-x@ 1 sylvain staff 18 Jan 25 00:19 0-current_working_directory
     -rwxr-xr-x@ 1 sylvain staff 19 Jan 25 00:23 1-listit
     ```

5. **4. Hidden files**
   - **File:** `4-listmorefiles`
   - **Description:** Display current directory contents, including hidden files (starting with `.`) in long format.
   - **Example:**
     ```sh
     $ ./4-listmorefiles
     total 32
     drwxr-xr-x@ 6 sylvain staff 204 Jan 25 00:29 .
     drwxr-xr-x@ 43 sylvain staff 1462 Jan 25 00:19 ..
     ```

6. **5. I love numbers**
   - **File:** `5-listfilesdigitonly`
   - **Description:** Display current directory contents in long format with user and group IDs displayed numerically and including hidden files.
   - **Example:**
     ```sh
     $ ./5-listfilesdigitonly
     total 32
     drwxr-xr-x@ 6 501 20 204 Jan 25 00:29 .
     drwxr-xr-x@ 43 501 20 1462 Jan 25 00:19 ..
     ```

7. **6. Welcome**
   - **File:** `6-firstdirectory`
   - **Description:** Create a script that creates a directory named `my_first_directory` in the `/tmp/` directory.
   - **Example:**
     ```sh
     $ ./6-firstdirectory
     $ file /tmp/my_first_directory/
     /tmp/my_first_directory/: directory
     ```

8. **7. Betty in my first directory**
   - **File:** `7-movethatfile`
   - **Description:** Move the file `betty` from `/tmp/` to `/tmp/my_first_directory/`.
   - **Example:**
     ```sh
     $ ./7-movethatfile
     $ ls /tmp/my_first_directory/
     betty
     ```

9. **8. Bye bye Betty**
   - **File:** `8-firstdelete`
   - **Description:** Delete the file `betty` in `/tmp/my_first_directory`.
   - **Example:**
     ```sh
     $ ./8-firstdelete
     $ ls /tmp/my_first_directory/
     ```

10. **9. Bye bye My first directory**
    - **File:** `9-firstdirdeletion`
    - **Description:** Delete the directory `my_first_directory` that is in the `/tmp` directory.
    - **Example:**
      ```sh
      $ ./9-firstdirdeletion
      $ file /tmp/my_first_directory
      /tmp/my_first_directory: cannot open `/tmp/my_first_directory' (No such file or directory)
      ```

11. **10. Back to the future**
    - **File:** `10-back`
    - **Description:** Write a script that changes the working directory to the previous one.
    - **Example:**
      ```sh
      julien@ubuntu:/tmp$ source ./10-back
      /tmp
      ```

12. **11. Lists**
    - **File:** `11-lists`
    - **Description:** Write a script that lists all files (even ones with names beginning with a period character, which are normally hidden) in the current directory and the parent of the working directory and the `/boot` directory (in this order), in long format.

13. **12. File type**
    - **File:** `12-file_type`
    - **Description:** Write a script that prints the type of the file named `iamafile`. The file `iamafile` will be in the `/tmp` directory when we will run your script.
    - **Example:**
      ```sh
      $ ./12-file_type
      /tmp/iamafile: ELF 64-bit LSB executable, x86-64, version 1 (SYSV), dynamically linked (uses shared libs), for GNU/Linux 2.6.24, BuildID[sha1]=bd39c07194a778ccc066fc963ca152bdfaa3f971, stripped
      ```

14. **13. We are symbols, and inhabit symbols**
    - **File:** `13-symbolic_link`
    - **Description:** Create a symbolic link to `/bin/ls`, named `__ls__`. The symbolic link should be created in the current working directory.
    - **Example:**
      ```sh
      $ ./13-symbolic_link
      $ ls -la
      lrwxrwxrwx  1 ubuntu ubuntu      7 Sep 20 03:24 __ls__ -> /bin/ls
      ```

15. **14. Copy HTML files**
    - **File:** `14-copy_html`
    - **Description:** Create a script that copies all the HTML files from the current working directory to the parent of the working directory, but only copy files that did not exist in the parent of the working directory or were newer than the versions in the parent of the working directory. You can consider that all HTML files have the extension `.html`.

## Advanced Tasks

1. **15. Let’s move**
   - **File:** `100-lets_move`
   - **Description:** Create a script that moves all files beginning with an uppercase letter to the directory `/tmp/u`. You can assume that the directory `/tmp/u` will exist when we will run your script.
   - **Example:**
     ```sh
     $ ./100-lets_move
     ```

2. **16. Clean Emacs**
   - **File:** `101-clean_emacs`
   - **Description:** Create a script that deletes all files in the current working directory that end with the character `~`.
   - **Example:**
     ```sh
     $ ./101-clean_emacs
     ```

3. **17. Tree**
   - **File:** `102-tree`
   - **Description:** Create a script that creates the directories `welcome/`, `welcome/to/`, and `welcome/to/school` in the current directory. You are only allowed to use two spaces (and lines) in your script, not more.
   - **Example:**
     ```sh
     $ ./102-tree
     ```

4. **18. Life is a series of commas, not periods**
   - **File:** `103-commas`
   - **Description:** Write a command that lists all the files and directories of the current directory, separated by commas (,).
     - Directory names should end with a slash (/)
     - Files and directories starting with a dot (.) should be listed
     - The listing should be alpha ordered, except for the directories `.` and `..` which should be listed at the very beginning
     - Only digits and letters are used to sort; digits should come first
     - You can assume that all the files we will test with will have at least
     - You can assume that all the files we will test with will have at least one letter or one digit
   - **Listing should end with a new line**
   - **Example:**
     ```sh
     $ ./103-commas
     ./, ../, 0-commas, 0-commas-checks/, 1-empty_casks, 2-gifs, 3-directories, 4-zeros, 5-rot13, 6-odd, 7-sort_rot13, Makefile, quote, .test, test_dir/, test.var
     ```

19. **19. File type: School**
   - **File:** `school.mgc`
   - **Description:** Create a magic file `school.mgc` that can be used with the command `file` to detect School data files. School data files always contain the string SCHOOL at offset 0.
   - **Example:**
     ```sh
     $ cp /bin/ls .
     $ ls -la
     total 268
     drwxrwxr-x  2 ubuntu ubuntu   4096 Sep 20 02:44 .
     drwxrwxrwt 11 root   root   139264 Sep 20 02:44 ..
     -rw-r--r--  1 ubuntu ubuntu    496 Sep 20 02:42 school.mgc
     -rwxr-xr-x  1 ubuntu ubuntu 110080 Sep 20 02:43 ls
     -rw-rw-r--  1 ubuntu ubuntu     50 Sep 20 02:06 thisisaschoolfile
     -rw-rw-r--  1 ubuntu ubuntu     30 Sep 20 02:16 thisisatextfile
     $ file -m school.mgc *
     school.mgc:         data
     ls:                  data
     thisisaschoolfile:   School data
     thisisatextfile:     ASCII text
     ```

## Contact

For any questions or suggestions, please contact me at:

Your Name - [your.email@example.com](mailto:your.email@example.com)

Project Link: [https://github.com/yourusername/alx-journey-system-engineering-devops](https://github.com/yourusername/alx-journey-system-engineering-devops)
