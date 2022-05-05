# Bit-Animation-Editor-UE5
This project contains a Unreal 5 project and plugin to import [Bit Animation Editor](https://store.steampowered.com/app/1370650/Bit__Animation_Editor/) asset into the engine. 

[![Ihttps://www.youtube.com/watch?v=5zEqkd6g8ms](https://img.youtube.com/vi/5zEqkd6g8ms/0.jpg)](https://www.youtube.com/watch?v=5zEqkd6g8ms)

[https://www.youtube.com/watch?v=5zEqkd6g8ms](https://www.youtube.com/watch?v=5zEqkd6g8ms)



### 🎨 How To Use
1. Create a new animation in [Bit Animation Editor](https://store.steampowered.com/app/1370650/Bit__Animation_Editor/).
2. Create a folder called ``BitAnimations`` final path should be ```/Content/BitAnimations```

*Unreal 5 will try to convert any imported JSON files but we need the Raw Json file.*

3. in Unreal 5 create a folder that matched your bit project name inside the ```/Content/BitAnimations/your-project``` folder
4. Go back to Bit and click ``Export/Export Unreal 5 Assets`` 
5. Select the Unreal 5 project folder. 
6. For the DataTable select ``BitProject``
7. In Unreal 5, right click any sprite and Select ``Scripted Asset Actions/Bit Animation Editor/Generate Project - Default``
8. type the name of your project.
9. Your sprites will now be configured and Flipbook animations will be created if they dont exist. 
10. A new assets called ``BitProjectBP`` will be added to your scene!

### 🚀 Faster Itteration
1. Edit an already imported project in Bit
2. Click  ``Export/Export JSON Array``
3. Generate a new asset (step 7 above).  



### 📦 How To Import only the plugin
As of writting this the Unreal 5 Marketplace dosen't support plugins that dosen't contain C++ code.
This importer is written with Blueprints and Python so in order to import this to your project here are some great workarounds...

1. Download the latest release zip of the plugin from here https://github.com/MorgondagDev/Bit-Animation-Editor-UE5/releases
2. Make sure your Unreal 5 project contains atleast one 2d sprite. 
3. Create a new Unreal plugin by going to Edit/Plugins then clicking Add.
4. Name the project BitAnimationEditor
5. Unzip the latest release and replace your local assets with the ones from the zip. 
6. You can now follow the "How To Use" guideliness. 
