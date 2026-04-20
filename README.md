## Windows Multi Bar
### About
**WMBar** -- is an application for searching information, 
executing files, and much more.
MBar is for those who value their time. MBar is speed.

---
### How to use?
**Press "Ctrl+Space"** to open the application.  
In the window that opens, enter the ***URL***, ***command***, or ***keyword***.

You can also open the system tray and right-click on the WMBar icon.  
And click the **"Показать"** button in the drop-down list.
---
### About Commands
A ***command*** is an instruction to perform some action.

### What do they look like?
Commands have a `!` before the keyword and also require flags depending on the task (example flag: `--flag`)
> ***Tip:*** If the flag documentation does not contain *REQUIRED, then it is not necessary to write the data after the flag.
---
### Available Commands
### Command: `!create`
**Creates** a file at the given path, with the given name and extension.

**flags**  
`--path Path:\To\Your\Folder` After the `--path` flag, you need to specify the save path, otherwise the default folder is the ***Documents*** folder.

`--name Your_file_name` After the `--name` flag, you need to specify the save name, otherwise the default name is the ***new_file***.

`--ext .extension` After the `--ext` flag, you need to specify the save extension, otherwise the default extension is the ***.txt*** extension.

---

### About Keywords
***Keywords*** are a simplified form of commands that do not require flags and only require data.

### What do they look like?
Keywords **don't** have any signs before the word as shown in the commands, keywords are **just words** followed by some data (example: `keyword Some data`)

> ***Tip:*** If the "requires data" column says NO, then after this keyword, you do not need to enter data.

### Types of Keywords
| Type            | What do they do                                                                                                                                                                             |
|-----------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Search keywords | If you specify data after these keywords, a link will open in the browser with some source in which this data will be searched. (example: `yt Fanny Videos` or `reddit How to touch grass`) |

### Search keywords
**List of all** available search keywords

| keywords             | service           | requires data |
|----------------------|-------------------|---------------|
| google, g, search    | Google.com        | No            |
| yt, youtube          | youtube.com       | No            |
| spotify              | spotify.com       | No            |
| pinterest            | pinterest.com     | No            |
| github               | github.com        | No            |
| pypi                 | pypi.org          | No            |
| stackoverflow, sflow | stackoverflow.com | No            |
| wikipedia, wiki      | wikipedia.com     | No            |
| rwikipedia, rwiki    | ru.wikipedia.com  | No            |
| reddit, r            | reddit.com        | No            |


### URL's
Instead of commands or keywords, you can simply  paste a URL into the WMBar panel, and it will open in your browser.  
**example:** `https://www.youtube.com/watch?v=dQw4w9WgXcQ`