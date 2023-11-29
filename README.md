<details close>
    <summary>Requeriments</summary>
    
    `
    pip install opencv-python
    pip install scikit-learn
    `

</details>

<details close>
    <summary>Possible errors</summary>
    
    #### If you have this error:
    ```console
    Traceback (most recent call last):
        File "/workspaces/Trabalho-Final-IA/main.py", line 1, in <module>
            import cv2
        File "/home/codespace/.python/current/lib/python3.10/site-packages/cv2/__init__.py", line 181, in <module>
            bootstrap()
        File "/home/codespace/.python/current/lib/python3.10/site-packages/cv2/__init__.py", line 153, in bootstrap
            native_module = importlib.import_module("cv2")
        File "/home/codespace/.python/current/lib/python3.10/importlib/__init__.py", line 126, in import_module
            return _bootstrap._gcd_import(name[level:], package, level)
    ImportError: libGL.so.1: cannot open shared object file: No such file or directory
    ```
    #### Solution:
    `
    sudo apt install libgl1-mesa-glx -y
    `

</details>