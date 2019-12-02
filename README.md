# ak-nvda-addon

## How to install:

1. Create the following directory: `%APPDATA%/NVDA/addons/ak-nvda-addon`
2. Copy/Paste contents of `/src` into directory from step 1.
3. Restart NVDA.

## Inter-process communication (IPC)

This addon uses a file-based IPC to communicate with Zamok. The addon will write "true" or "false" to the `.dat` file while Zamok will monitor that file for changes and update it's state accordingly.

File Location: `%LOCALAPPDATA%/ZamokNVDA.dat`
