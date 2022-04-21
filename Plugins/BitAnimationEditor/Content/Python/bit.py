from array import array
from pickle import FALSE
import unreal
import json
import sys

inputFile = sys.argv[1]

print("input argument: " + inputFile)
fObj = open(inputFile)
jsonData = json.load(fObj)[0]
fObj.close()

asset_tools = unreal.AssetToolsHelpers.get_asset_tools()
spritefactory = unreal.PaperSpriteFactory()
flipbookFactory = unreal.PaperFlipbookFactory()
blueprintFactory = unreal.BlueprintFactory()
blueprintFactory.set_editor_property("ParentClass", unreal.Actor)

projectName = jsonData["name"].replace(" ", "")

def setupTextureSettings():
    for asset in jsonData["assets"]:
        texture = unreal.Texture2D.cast(unreal.EditorAssetLibrary.load_asset("/Game/BitAnimations/"+projectName+"/"+asset["id"].replace(" ", "")))
        #unreal.TextureRenderTargetFormat.RTF_RGBA8_SRGB
        texture.set_editor_property("lod_group", unreal.TextureGroup.TEXTUREGROUP_PIXELS2D)
        texture.set_editor_property("compression_settings", unreal.TextureCompressionSettings.TC_EDITOR_ICON)
        unreal.EditorAssetLibrary.save_loaded_asset(texture, False)




def createBackground():
    texture = unreal.Texture2D.cast(unreal.EditorAssetLibrary.load_asset("/Game/BitAnimations/"+projectName+"/background"))
    projectSize = unreal.Vector2D( jsonData["width"], jsonData["height"])
    newSprite = unreal.PaperSprite.cast(asset_tools.create_asset("background", "/Game/BitAnimations/"+projectName+"/assets/", None, spritefactory) )
    newSprite.set_editor_property("source_texture", texture)
    newSprite.set_editor_property("source_dimension", projectSize)
    newSprite.set_editor_property("source_texture_dimension", projectSize)
    newSprite.set_editor_property("pivot_mode", unreal.SpritePivotMode.CENTER_CENTER)
    newSprite.set_editor_property("source_uv", unreal.Vector2D( 
        0,
        0,
    ))
    newSprite.set_editor_property("trimmed_in_source_image", True)
    newSprite.set_editor_property("trimmed_in_source_image", False)
    unreal.EditorAssetLibrary.save_loaded_asset(newSprite, False)
    newSprite.set_editor_property("source_uv", unreal.Vector2D( 
        0,
        0,
    ))
  


def createAssets():
    with unreal.ScopedSlowTask(len(jsonData["assets"]), "Creating Assets") as slow_task:
        slow_task.make_dialog(True)
        
        currentAssetCount = 0

        for asset in jsonData["assets"]:

            print("Setup asset for "+asset['id'])

            currentAssetCount += 1
            slow_task.enter_progress_frame(currentAssetCount)

            id = asset['id']
            tileSize = unreal.Vector2D(asset["tileSize"]["x"], asset["tileSize"]["y"])
            spriteSize = unreal.Vector2D(asset["spriteSize"]["x"], asset["spriteSize"]["y"])
            texture = unreal.Texture2D.cast(unreal.EditorAssetLibrary.load_asset("/Game/BitAnimations/"+projectName+"/"+asset["id"].replace(" ", "")))
            xTiles = int(spriteSize.x / tileSize.x)
            yTiles = int(spriteSize.y / tileSize.y)
            currentTile = 1

            for ytile in list(range(1,yTiles+1)):
                for xtile in list(range(1,xTiles+1)):
                    newSprite = unreal.PaperSprite.cast(asset_tools.create_asset(str(currentTile), "/Game/BitAnimations/"+projectName+"/assets/"+id+"/sprites".replace(" ", ""), None, spritefactory) )
                    newSprite.set_editor_property("source_texture", texture)
                    newSprite.set_editor_property("source_dimension", tileSize)
                    newSprite.set_editor_property("source_texture_dimension", spriteSize)
                    newSprite.set_editor_property("pivot_mode", unreal.SpritePivotMode.CENTER_CENTER)
                    newSprite.set_editor_property("source_uv", unreal.Vector2D( 
                        (xtile-1) * tileSize.x,
                        (ytile-1) * tileSize.y,
                    ))
                    newSprite.set_editor_property("trimmed_in_source_image", True)
                    newSprite.set_editor_property("trimmed_in_source_image", False)
                    
                    unreal.EditorAssetLibrary.save_loaded_asset(newSprite, False)
                    newSprite.set_editor_property("source_uv", unreal.Vector2D( 
                        (xtile-1) * tileSize.x,
                        (ytile-1) * tileSize.y,
                    ))
                    currentTile += 1
            
            print(id)
            defaultFlipbook = unreal.PaperFlipbook.cast(asset_tools.create_asset("default", "/Game/BitAnimations/"+projectName+"/assets/"+id+"/animations".replace(" ", ""), None, flipbookFactory) )
            defaultFlipbook.set_editor_property("frames_per_second", 0.0)
            defaultFrame = unreal.PaperFlipbookKeyFrame()
            defaultFrame.set_editor_property("sprite",unreal.PaperSprite.cast(unreal.EditorAssetLibrary.load_asset( "/Game/BitAnimations/"+projectName+"/assets/"+id+"/sprites/1".replace(" ", "")) ))
            defaultFrame.set_editor_property("frame_run",1)
            defaultFlipbook.set_editor_property("key_frames", [defaultFrame])
            unreal.EditorAssetLibrary.save_loaded_asset(defaultFlipbook, False)
            
            animations = asset["animations"]
            currentAnimation = 0
            for animation in animations:
                print(animation["name"])
                newFlipbook = unreal.PaperFlipbook.cast(asset_tools.create_asset(str(animation["name"].replace(" ", "")), "/Game/BitAnimations/"+projectName+"/assets/"+id+"/animations".replace(" ", ""), None, flipbookFactory) )
                newFlipbook.set_editor_property("frames_per_second", 45-float(animation["frameskip"]*10))
                ##frame1.set_editor_property("sprite")
                animationFrames = []

                for tile in animation["tiles"]:
                    frame = unreal.PaperFlipbookKeyFrame()
                    spritePath = "/Game/BitAnimations/"+projectName+"/assets/"+id+"/sprites/" + str(tile+1).replace(" ", "")
                    frameSprite = unreal.PaperSprite.cast(unreal.EditorAssetLibrary.load_asset( spritePath ) )
                    frame.set_editor_property("sprite",frameSprite)
                    frame.set_editor_property("frame_run",1)
                    animationFrames.append(frame)

                newFlipbook.set_editor_property("key_frames", animationFrames)
                unreal.EditorAssetLibrary.save_loaded_asset(newFlipbook, False)
                currentAnimation+=1

    
        slow_task.make_dialog(False)


try:
    backgroundAsset = unreal.PaperSprite.cast(unreal.EditorAssetLibrary.load_asset("/Game/BitAnimations/"+projectName+"/assets/background"))
    print("skipping asset pipeline, already generated. To regenerate remote project /assets/ folder")
except:
    setupTextureSettings()
    createAssets()
    createBackground()
