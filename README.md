# ascii-cam
Simple cli application for ascii effects on terminal from camera feed. 

![image](/misc/ascii-cam.png)

## Installation
- First clone the repository
    ```
    git clone https://github.com/Acedev003/ascii-cam.git
    ```
- Install dependencies ( imageio[ffmpeg] )
    ```
    pip install -r requirements.txt
    ```
- Run the program
    ```
    python src/ascii.py
    ```

## Command Line options

- For usage type
    ```
    python src/ascii.py [-h or --help] 
    ```

- By default the program uses the ascii density map 
    >  .:-=+*#%@

    To use a longer ascii density string 
    >  ..''``^\",:;Il!i><~+_-?][}{1)(|\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$
    
    the following option can be used
    ```
    python src/ascii.py [-l or --long] 
    ```

- To set the darkness level of the output use the -d | --darkness option
    ```
    python src/ascii.py [-d or --darkness] darkness_level 
    ```
    where the darkness level lies in the range 0 - 50

