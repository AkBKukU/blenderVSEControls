bl_info = {
    "name": "Sequencer Controls",
    "category": "Sequencer",
}

import bpy


def menu_func(self, context):
    layout = self.layout
    scene = context.scene
    screen = context.screen
    userprefs = context.user_preferences

    row = layout.row(align=True)
    if not scene.use_preview_range:
        row.prop(scene, "frame_start", text="Start")
        row.prop(scene, "frame_end", text="End")
    else:
        row.prop(scene, "frame_preview_start", text="Start")
        row.prop(scene, "frame_preview_end", text="End")

    layout.prop(scene, "frame_current", text="")

    layout.separator()

    row = layout.row(align=True)
    row.operator("screen.frame_jump", text="", icon='REW').end = False
    row.operator("screen.keyframe_jump", text="", icon='PREV_KEYFRAME').next = False
    if not screen.is_animation_playing:
        # if using JACK and A/V sync:
        #   hide the play-reversed button
        #   since JACK transport doesn't support reversed playback
        if scene.sync_mode == 'AUDIO_SYNC' and context.user_preferences.system.audio_device == 'JACK':
            sub = row.row(align=True)
            sub.scale_x = 2.0
            sub.operator("screen.animation_play", text="", icon='PLAY')
        else:
            row.operator("screen.animation_play", text="", icon='PLAY_REVERSE').reverse = True
            row.operator("screen.animation_play", text="", icon='PLAY')
    else:
        sub = row.row(align=True)
        sub.scale_x = 2.0
        sub.operator("screen.animation_play", text="", icon='PAUSE')
    row.operator("screen.keyframe_jump", text="", icon='NEXT_KEYFRAME').next = True
    row.operator("screen.frame_jump", text="", icon='FF').end = True



def register():
    bpy.types.SEQUENCER_HT_header.append(menu_func)


def unregister():
    bpy.types.SEQUENCER_HT_header.remove(menu_func)


if __name__ == "__main__":
    register()

