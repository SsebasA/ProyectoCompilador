# Running the Generated WAT Code in the Browser

Assuming the Delta compiler generates correct WAT code, call the `realize` method with the `Phase.CODE_GENERATION` argument. For example:

```python
from delta import Compiler, Phase

source_code = '42'
c = Compiler('program')
c.realize(source_code, Phase.CODE_GENERATION)
```

Running the preceding code creates an `output.wat` file within the `web` folder. To execute this file in a browser, we first need to translate it into a WASM binary file. This can be done by following these steps:

- Download the `wat2wasm` program for your specific platform and place it in the `web` folder:

    - Windows x64: [wat2wasm.exe](https://arielortiz.info/s202611/tc3002b/wat2wasm/windows_x64/wat2wasm.exe)
    - macOS ARM64: [wat2wasm](https://arielortiz.info/s202611/tc3002b/wat2wasm/macos_arm64/wat2wasm)
    - Linux x64: [wat2wasm](https://arielortiz.info/s202611/tc3002b/wat2wasm/linux_x64/wat2wasm)
    - Linux ARM64: [wat2wasm](https://arielortiz.info/s202611/tc3002b/wat2wasm/linux_arm64/wat2wasm)

- Assemble the `output.wat` from within the `web` folder.

    - In **Windows**, at the CMD or PowerShell terminal type:
        ```
        .\wat2wasm.exe output.wat
        ```

    - In **macOS** and **Linux**, at the terminal type:
        ```
        ./wat2wasm output.wat
        ```

Now, we can execute the WASM code within a browser. At the terminal, from the `web` folder run the following command to start a simple web server:

    python -m http.server

Open a web browser (Google Chrome is recommended due to its fine WebAssembly debugging tools) and enter the following in the address bar:

    localhost:8000

The numeric result of the execution should then be displayed as part of the `index.html` web page.

You can open the developer tools on Chrome (`Ctrl+Shift+I` on Windows and Linux, or `Option-Command-I` on macOS) to utilize the debugger. Navigate to the `Sources` tab and locate the WebAssembly code under the `wasm` node. You can then place a code breakpoint and reload the page to start single-stepping through the WASM code.
