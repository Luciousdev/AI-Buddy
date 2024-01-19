# AI Buddy (neuro sama off of wish)

## Requirements

| **Package** | **Version**   |
|-------------|---------------|
| python      | ">=3.9 <3.12" |
| pip         | ">=23.3.2"    |
| c++ build tools | ">=14.0" |
### Compatibility
| OS      | Status  |
|---------|---------|
| Linux   | ✅       |
| Windows | ✅       |
| MacOS   | ❔       |
| Android | 🚧      |
✅ = Currently Supported<br>
🚧 = Working on support/still being tested<br>
❔ = Not able to test support<br>
❌ = Not supported

## How to install

```commandline
git clone https://github.com/Luciousdev/AI-Buddy.git
cd AI-Buddy
pip3 install -r requirements.txt
```

### Windows specific
1. If you are on windows you need to make sure that you have the c++ build tools version 14.0 or higher (14.0 prefered).
Here is a [guide](https://stackoverflow.com/questions/64261546/how-to-solve-error-microsoft-visual-c-14-0-or-greater-is-required-when-inst) on how to install it if you haven't.
2. Make sure that you disable (at least temporarily to install the packages) the maximum path length limitation. Microsoft has a guide [here](https://learn.microsoft.com/en-us/windows/win32/fileio/maximum-file-path-limitation?tabs=powershell#enable-long-paths-in-windows-10-version-1607-and-later)
3. If you get an error when trying to use cude make sure that you have [installed pytorch correctly](https://stackoverflow.com/questions/57238344/i-have-a-gpu-and-cuda-installed-in-windows-10-but-pytorchs-torch-cuda-is-availa) (also make sure that you have the cuda drivers.)