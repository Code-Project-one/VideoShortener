# VideoShortener
This Script will take a long video clip and cut it to 60 sec.
---------------------
Create a new directory for your project (if you haven't already done so).

Open a terminal or command prompt and navigate to the project directory.

## Create a new virtual environment by running the following command:

```
python -m venv myenv
```
This will create a new virtual environment named myenv in the project directory.

Activate the virtual environment. The commands for activation differ depending on your operating system:

On Windows:
```
myenv\Scripts\activate
```

On macOS and Linux:
```
source myenv/bin/activate
```

After activating the virtual environment, you should see (myenv) at the beginning of your command prompt, indicating that you are now working within the virtual environment.

Install the required dependencies, including moviepy, by running the following command:
```
pip install moviepy
```

This will install moviepy and its necessary dependencies within the virtual environment.
Now you can create your video_splitter.py file (as mentioned in the previous instructions) and run the script using the python command:
```
python video_splitter.py
```

The script will run within the activated virtual environment, and the video-splitting process will be executed accordingly.

Remember to activate the virtual environment each time you want to run the script. If you finish working on the project, you can deactivate the virtual environment by running the command deactivate.

----------------
Create a new directory for your project.

Inside the project directory, create a new Python script file with a .py extension, for example, video_splitter.py.

Open the ```video_splitter.py``` file and copy the code provided earlier.

Save the file.

In the same directory, place the large video file that you want to split.

Open a terminal or command prompt, navigate to the project directory, and run the script using the command ```python video_splitter.py```.


Using a virtual environment helps keep your project dependencies separate and avoids conflicts with other Python projects you may be working on.
