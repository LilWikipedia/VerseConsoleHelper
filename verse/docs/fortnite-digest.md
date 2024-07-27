---
layout:
  title:
    visible: true
  description:
    visible: true
  tableOfContents:
    visible: true
  outline:
    visible: true
  pagination:
    visible: true
---

# 📘 Fortnite Digest

## ui

### text\_button

* Button with text message common base class. Displays a button with a custom message string.

`text_button_base<native><public> := class<abstract><epic_internal>(widget):`

### DefaultText

* The text to display to the user. Used only during initialization of the widget and not modified by `SetText`.

`DefaultText<localizes><native><public>:message = external {}`

### OnClick

* Subscribable event that fires when the button is clicked.

`OnClick<public>():listenable(widget_message) = external {}`

### SetText

* Sets the text displayed in the widget.

`SetText<native><public>(InText:message):void`

### GetText

* Gets the text currently in the widget.

`GetText<native><public>():string`

### button\_loud

* Text button with big and loud styling applied.

`button_loud<native><public> := class<final>(text_button_base):`

### button\_regular

* Text button with normal styling applied.

`button_regular<native><public> := class<final>(text_button_base):`

### button\_quiet

* Text button with quiet styling applied.

`button_quiet<native><public> := class<final>(text_button_base):`

### HUDElements

* Shows a set of HUD elements.

`(PlayerUI:player_ui).ShowHUDElements<native><public>(HUDElements:[]hud_element_identifier):void`

* Hides a set of HUD elements.

`(PlayerUI:player_ui).HideHUDElements<native><public>(HUDElements:[]hud_element_identifier):void`

* Resets the visibility for a set of HUD elements.

`(PlayerUI:player_ui).ResetHUDElementVisibility<native><public>(HUDElements:[]hud_element_identifier):void`

### fort\_hud\_controller

* A HUD controller that allows for showing and hiding of HUD elements.

`fort_hud_controller<native><public> := interface<epic_internal>:`

* Shows a set of HUD elements.

`ShowElements<public>(HUDElements:[]hud_element_identifier):void`

* Hides a set of HUD elements.

`HideElements<public>(HUDElements:[]hud_element_identifier):void`

* Resets the visibility for a set of HUD elements.

`ResetElementVisibility<public>(HUDElements:[]hud_element_identifier):void`

* Get the `fort_hud_controller` for the current `fort_playspace`

`(Playspace:fort_playspace).GetHUDController<native><public>():fort_hud_controller`

### HUD Identifiers:

```
creative_hud_identifier_all<public> := class<final>(hud_element_identifier):

creative_hud_identifier_build_menu<public> := class<final>(hud_element_identifier):

creative_hud_identifier_crafting_resources<public> := class<final>(hud_element_identifier):

creative_hud_identifier_elimination_counter<public> := class<final>(hud_element_identifier):

creative_hud_identifier_equipped_item<public> := class<final>(hud_element_identifier):

creative_hud_identifier_experience_level<public> := class<final>(hud_element_identifier):

creative_hud_identifier_experience_supercharged<public> := class<final>(hud_element_identifier):

creative_hud_identifier_experience_ui<public> := class<final>(hud_element_identifier):

creative_hud_identifier_health<public> := class<final>(hud_element_identifier):

creative_hud_identifier_health_numbers<public> := class<final>(hud_element_identifier):

creative_hud_identifier_hud_info<public> := class<final>(hud_element_identifier):

creative_hud_identifier_interaction_prompts<public> := class<final>(hud_element_identifier):

creative_hud_identifier_map_prompts<public> := class<final>(hud_element_identifier):

creative_hud_identifier_mimimap<public> := class<final>(hud_element_identifier):

creative_hud_identifier_minimap<public> := class<final>(hud_element_identifier):

creative_hud_identifier_pickup_stream<public> := class<final>(hud_element_identifier):

creative_hud_identifier_player_count<public> := class<final>(hud_element_identifier):

creative_hud_identifier_player_inventory<public> := class<final>(hud_element_identifier):

creative_hud_identifier_round_info<public> := class<final>(hud_element_identifier):

creative_hud_identifier_round_timer<public> := class<final>(hud_element_identifier):

creative_hud_identifier_shield_numbers<public> := class<final>(hud_element_identifier):

creative_hud_identifier_shileds<public> := class<final>(hud_element_identifier):

creative_hud_identifier_shields<public> := class<final>(hud_element_identifier):

creative_hud_identifier_storm_notifications<public> := class<final>(hud_element_identifier):

creative_hud_identifier_storm_timer<public> := class<final>(hud_element_identifier):

creative_hud_identifier_team_info<public> := class<final>(hud_element_identifier):

player_hud_identifier_all<public> := class<final>(hud_element_identifier):

hud_identifier_world_resource_wood<public> := class<final>(hud_element_identifier):

hud_identifier_world_resource_stone<public> := class<final>(hud_element_identifier):

hud_identifier_world_resource_metal<public> := class<final>(hud_element_identifier):

hud_identifier_world_resource_permanite<public> := class<final>(hud_element_identifier):

hud_identifier_world_resource_gold_currency<public> := class<final>(hud_element_identifier):

hud_identifier_world_resource_ingredient<public> := class<final>(hud_element_identifier):
```

### hud\_element\_identifier

* Used to identify a HUD element.

`hud_element_identifier<native><public> := class<abstract><epic_internal>:`

### slider\_regular

* Slider with a text value. Displays a slider, its progress bar and value.

`slider_regular<native><public> := class<final>(widget):`

* The value to display to the user. Used only during initialization of the widget and not modified by `SetValue`

`DefaultValue<native><public>:float = external {}`

* The minimum value that the slider can haver. Used only during initialization of the widget and not modified by `SetMinValue`

`DefaultMinValue<native><public>:float = external {}`

* The maximum value that the slider can haver. Used only during initialization of the widget and not modified by `SetMaxValue`

`DefaultMaxValue<native><public>:float = external {}`

* The amount to adjust the value by, when using a controller or keyboard. Used only during initialization of the widget and not modified by `SetStepSize`

`DefaultStepSize<native><public>:float = external {}`

* Sets the value of the slider, will clamp the value to be within the sliders minimum and maximum value.

`SetValue<native><public>(InValue:float):void`

* Gets the value of the slider.

`GetValue<native><public>():float`

* Sets the minimum value of the slider, will enforce that the sliders maximum value is always larger than or equal to the minimum value.

`SetMinValue<native><public>(InMinValue:float):void`

* Gets the minimum value of the slider.

`GetMinValue<native><public>():float`

* Sets the maximum value of the slider, will enforce that the sliders maximum value is always larger than or equal to the minimum value.

`SetMaxValue<native><public>(InMaxValue:float):void`

* Gets the maximum value of the slider.

`GetMaxValue<native><public>():float`

* Sets the amount to adjust the value by, when using a controller or keyboard.

`SetStepSize<native><public>(InValue:float):void`

* Gets the amount to adjust the value by.

`GetStepSize<native><public>():float`

* Subscribable event that fires when the value of the slider has changed.

`OnValueChanged<public>():listenable(widget_message) = external {}`

### text\_block

* Text block widget. Displays text to the user.

`text_block<native><public> := class<final>(text_base):`

* The direction the shadow is cast. Used only during initialization of the widget and not modified by `SetShadowOffset`

`DefaultShadowOffset<native><public>:?vector2 = external {}`

* The color of the shadow. Used only during initialization of the widget and not modified by `SetShadowColor`

`DefaultShadowColor<native><public>:color = external {}`

* Sets the direction the shadow is cast.

`SetShadowOffset<native><public>(InShadowOffset:?vector2):void`

* Gets the direction the shadow is cast.

`GetShadowOffset<native><public>():?vector2`

* Sets the color of the shadow.

`SetShadowColor<native><public>(InColor:color):void`

* Gets the color of the shadow.

`GetShadowColor<native><public>():color`

* Sets the opacity of the shadow.

`SetShadowOpacity<native><public>(InOpacity:type {_X:float where 0.000000 <= _X, _X <= 1.000000}):void`

* Gets the opacity of the shadow.

`GetShadowOpacity<native><public>():type {_X:float where 0.000000 <= _X, _X <= 1.000000}`

***

## creative\_devices

### animation\_controller

* Animation := module:
* Module import path: `/Fortnite.com/Devices/Animation`

`CreativeAnimation<public> := module:`

* A structure for defining [Bezier interpolation](https://en.wikipedia.org/wiki/B%C3%A9zier\_curve) parameters.

`cubic_bezier_parameters<native><public> := struct<computes>:`

* X value of the P1 control point. `0.0 <= X0 <= 1.0` or an error will be generated when calling `animation_controller.SetAnimation`.

`X0<native><public>:float = external {}`

* Y value of the P1 control point.

`Y0<native><public>:float = external {}`

* X value of the P2 control point. `0.0 <= X1 <= 1.0` or an error will be generated when calling `animation_controller.SetAnimation`.

`X1<native><public>:float = external {}`

* Y value of the P2 control point.

`Y1<native><public>:float = external {}`

* Convenience interpolation modes. These built in modes are based on the [CSS animation standard](https://www.w3.org/TR/css-easing-1/)

#### Interpolation Types

* Convenience interpolation modes. These built in modes are based on the [CSS animation standard](https://www.w3.org/TR/css-easing-1/)
* `Linear` animations move at a constant speed.

`Linear<public>:cubic_bezier_parameters = external {}`

* `Ease` animations start slowly, speed up, then end slowly. The speed of the animation is slightly slower at the end than the start.

`Ease<public>:cubic_bezier_parameters = external {}`

* `EaseIn` animations start slow, then speed up towards the end.

`EaseIn<public>:cubic_bezier_parameters = external {}`

* `EaseOut` animations start fast, then slow down towards the end.

`EaseOut<public>:cubic_bezier_parameters = external {}`

* `EaseInOut` animations are similar to `Ease` but the start and end animation speed is symmetric.

`EaseInOut<public>:cubic_bezier_parameters = external {}`

* Instead of specifying the actual keyframe positions, we specify the keyframe deltas. This allows us to treat the initial position of the prop as keyframe 0 and avoid the question of how to get the prop to its initial location. For a `animation_mode.Loop` animation, the net rotation and translation must both be zero. Each delta is interpreted as a world-space transformation to be concatenated onto the previous transform(s).

`keyframe_delta<native><public> := struct:`

* Target position of the `creative_prop`. This is a world-space coordinate in cm, with the initial position of the `creative_prop` acting as coordinate (0,0).

`DeltaLocation<native><public>:vector3`

* Target rotation for the `creative_prop`. Rotations are relative to the starting rotation of the `creative_prop`

`DeltaRotation<native><public>:rotation`

* Target scale for the `creative_prop`. Scale is multiplicative to the starting Scale of the `creative_prop`

`DeltaScale<native><public>:vector3 = external {}`

* Time in seconds the `creative_prop` should animate between its last frame and this frame.

`Time<native><public>:float`

* Interpolation mode for this `keyframe_delta`
* Default = `InterpolationTypes.Linear`

`Interpolation<native><public>:cubic_bezier_parameters = external {}`

* Animation play modes.

`animation_mode<native><public> := enum:`

* Stop after playing the animation once.

`OneShot`

* Reverse direction after reaching the final `keyframe_delta`, then play the animation in reverse.

`PingPong`

* Play the animation in a loop. This requires the animation ends exactly where it began.

`Loop`

* `animation_controller` states.

`animation_controller_state<native><public> := enum:`

* The target of the animation is not an animatable prop. This could be because:
* It is not a `creative_prop` that can be animated.
* It was disposed or otherwise destroyed.
* It has the 'Register with Structural Grid' option set in UEFN.

`InvalidObject`

* No animation has been successfully set via `animation_controller.SetAnimation`, or that animation has been cleared by a failed call to `animation_controller.SetAnimation`

`AnimationNotSet`

* Animation has either never started, finished, or was explicitly stopped.

`Stopped`

* Animation is playing.

`Playing`

* Animation is paused.

`Paused`

* Results for `animation_controller.AwaitNextKeyframe` function.

`await_next_keyframe_result<native><public> := enum:`

* The next keyframe has been reached successfully.

`KeyframeReached`

* No animation is currently playing and this function call has returned immediately.

`NotPlaying`

* The animation was canceled either due to the object being destroyed, becoming invalid, or because it was moved via some other API.

`AnimationAborted`

* Used to move and animate the position of `creative_prop` objects.
* See `creative_prop.GetAnimationController` for information on acquiring an instance of an `animation_controller` for a given `creative_prop`.
* See `SetAnimation` for details on authoring movement and animations.

`animation_controller<native><public> := class<epic_internal>:`

* Suspends at the callsite until the next `keyframe_delta` is finished. This will also return if the animation is aborted or not playing. See `await_next_keyframe_result` if your code needs to take different paths based on why `AwaitNextKeyframe` returned.

`AwaitNextKeyframe<native><public>()<suspends>:await_next_keyframe_result`

* Starts or resumes playback of the animation.

`Play<public>():void = external {}`

* Pauses the animation if it is already playing.

`Pause<public>():void = external {}`

* Stops playback and resets the animation to the first keyframe. Also resets the prop transform. Calling this method is valid while the animation is in the `Playing` or `Paused` states.

`Stop<public>():void = external {}`

* Returns the current state of this `animation_controller`.

`GetState<native><public>()<transacts>:animation_controller_state`

* Succeeds if this `animation_controller`s target is still valid (i.e., the target has not been disposed of either via `Dispose` or through any external system.)

`IsValid<native><public>()<transacts><decides>:void`

* Sets the animation for the `animation_controller`. Animations are processed in the order provided in `Keyframes`.

`SetAnimation<public>(Keyframes:[]keyframe_delta, ?Mode:animation_mode):void = external {}`

* Signaled each time a keyframe is reached. Callback(KeyframeIndex:int, InReverse:logic). Note that the KeyframeIndex in the callback is generally in \[1, NumDeltaKeyframes] except that in a `PingPong` animation the final keyframe played in reverse is identified as index 0. This is because `SetAnimation` takes delta keyframes whereas this event notifies the listener that a specific keyframe has been reached.

`KeyframeReachedEvent<native><public>:listenable(tuple(int, logic)) = external {}`

* Signaled when the entire animation is complete. This will only fire for `OneShot` animations.

`MovementCompleteEvent<native><public>:listenable(tuple()) = external {}`

* Signaled when the state has changed. Use `GetState` to get the new state.

`StateChangedEvent<native><public>:listenable(tuple()) = external {}`

* Returns an `animation_controller` used to animate `Prop`. Only a subset of `creative_prop` types can be animated, though this may change in the future. A few examples of props that cannot be animated yet are: Walls attached to buildings, treasure chests, and Llamas.

`(Prop:creative_prop).GetAnimationController<public>()<transacts><decides>:animation_controller = external {}`

### creative\_device

`creative_device<native><public> := class<concrete>(creative_object_interface):`

* Inherit from this to create a custom creative device. Inherited classes will appear in the UEFN content browser the next time Verse compiles. Instances of your derived `creative_device` can then be placed in the island by dragging them from the content browser into the scene.
* Override to add custom logic when the game experience begins.

`OnBegin<native_callable><public>()<suspends>:void = external {}`

* Override to add custom logic when the game experience ends. Any coroutines spawned inside `OnEnd` may never execute.

`OnEnd<native_callable><public>():void = external {}`

* Returns the transform of the `creative_device` with units in cm.

`GetTransform<override>()<transacts>:transform = external {}`

* Teleports the `creative_device` to the specified `Position` and `Rotation`.

`TeleportTo<public>(Position:vector3, Rotation:rotation)<transacts><decides>:void = external {}`

* Teleports the `creative_device` to the specified location defined by `Transform`, also applies rotation and scale accordingly.

`TeleportTo<public>(Transform:transform)<transacts><decides>:void = external {}`

* Moves the `creative_device` to the specified `Position` and `Rotation` over the specified time, in seconds. If an animation is currently playing on the `creative_device` it will be stopped and put into the `AnimationNotSet` state.

`MoveTo<public>(Position:vector3, Rotation:rotation, OverTime:float)<suspends>:move_to_result = external {}`

* Moves the `creative_device` to the specified `Transform` over the specified time, in seconds. If an animation is currently playing on the `creative_device` it will be stopped and put into the `AnimationNotSet` state.

`MoveTo<public>(Transform:transform, OverTime:float)<suspends>:move_to_result = external {}`

* Shows this device in the world.

`Show<native><public>()<transacts>:void`

* Hides this device in the world.

`Hide<native><public>()<transacts>:void`

* Base class for creative\_device.

`creative_device_base<native><public> := class<abstract><epic_internal>(creative_object):`

* Internal asset for representing creative devices.

`creative_device_asset<native><public> := class<computes><final><epic_internal>:`

`creative_object_interface<native><public> := interface<epic_internal>(positional):`

* Base class for creative devices and props.

`creative_object<native><public> := class<epic_internal>(creative_object_interface):`

* Returns the transform of the `creative_object` with units in cm. You must check `creative_object.IsValid` before calling this if there is a possibility the object has been disposed or destroyed by gameplay.

`GetTransform<override>()<transacts>:transform = external {}`

* Teleports the `creative_object` to the specified `Position` and `Rotation`.

`TeleportTo<public>(Position:vector3, Rotation:rotation)<transacts><decides>:void = external {}`

* Teleports the `creative_object` to the specified location defined by `Transform`, also applies rotation and scale accordingly.

`TeleportTo<public>(Transform:transform)<transacts><decides>:void = external {}`

* Moves the `creative_object` to the specified `Position` and `Rotation` over the specified time, in seconds. If an animation is currently playing on the `creative_object` it will be stopped and put into the `AnimationNotSet` state.

`MoveTo<public>(Position:vector3, Rotation:rotation, OverTime:float)<suspends>:move_to_result = external {}`

* Moves the `creative_object` to the specified `Transform` over the specified time, in seconds. If an animation is currently playing on the `creative_object` it will be stopped and put into the `AnimationNotSet` state.

`MoveTo<public>(Transform:transform, OverTime:float)<suspends>:move_to_result = external {}`

* Returns an array containing all creative objects which have been marked with the specified `Tag`.

`GetCreativeObjectsWithTag<native><public>(Tag:tag)<transacts>:[]creative_object_interface`

* Returns an array containing creative objects which have tag(s) matching the specified `SearchCriteria`.

`GetCreativeObjectsWithTags<native><public>(SearchCriteria:tag_search_criteria)<transacts>:[]creative_object_interface`

* Returns a queryable `tag_view` which can be used to query the tags on `CreativeObject`.

`(CreativeObject:creative_object_interface).GetTags<native><public>():tag_view`

* Returns the `fort_playspace` that `CreativeObject` belongs to.

`(CreativeObject:creative_object_interface).GetPlayspace<native><public>()<transacts>:fort_playspace`

* A Fortnite prop that has been placed or spawned in the island.

`creative_prop<native><public> := class<concrete><final>(creative_object, invalidatable):`

* Destroys the `creative_prop` and remove it from the island.

`Dispose<native><override>():void`

* Succeeds if this object has not been disposed of either via `Dispose()` or through an external system.

`IsValid<native><override>()<transacts><decides>:void`

* Changes the Mesh used by this instance.

`SetMesh<native><public>(Mesh:mesh)<transacts>:void`

* Changes the Material of the Mesh used by this instance. Optionally can specify which Mesh element index to apply the material to, otherwise defaults to the 0 (default) Mesh element

`SetMaterial<native><public>(Material:material, ?Index:int = external {})<transacts>:void`

* Shows the `creative_prop` in the world and enable collisions.

`Show<native><public>()<transacts>:void`

* Hides the `creative_prop` in the world and disable collisions.

`Hide<native><public>()<transacts>:void`

### creative\_prop\_asset

* Asset used to spawn `creative_prop` instances.

`creative_prop_asset<native><public> := class<computes><concrete><final><epic_internal>:`

* A default asset to be used when creating an editor-specified `creative_prop_asset` variable.

`DefaultCreativePropAsset<public>:creative_prop_asset = external {}`

### SpawnProp

`spawn_prop_result<native><public> := enum:`

* Results for `SpawnProp`.
* The spawn point contains NaN or Inf.

`InvalidSpawnPoint`

* The spawn point is outside the island's boundaries.

`SpawnPointOutOfBounds`

* The asset is not a valid `creative_prop`.

`InvalidAsset`

* More props have been spawned than are permitted by the island's rules (currently 100 per script device and 200 total per island).

`TooManyProps`

* Spawns a `creative_prop` at the specified `Position` and `Rotation`. `Position` and `Rotation` units are in cm.
* Returns tuple:
* 0: Instance of a `creative_prop`. False if no `creative_prop` could be created. See `spawn_prop_result` for failure cases.
* 1: Success or failure results.

`SpawnProp<native><public>(Asset:creative_prop_asset, Position:vector3, Rotation:rotation)<transacts>:tuple(?creative_prop, spawn_prop_result)`

* Spawns a `creative_prop` at the specified `Transform`. \`Units are in cm.
* Returns tuple:
* 0: Instance of a `creative_prop`. False if no `creative_prop` could be created. See `spawn_prop_result` for failure cases.
* 1: Success or failure results.

`SpawnProp<native><public>(Asset:creative_prop_asset, Transform:transform)<transacts>:tuple(?creative_prop, spawn_prop_result)`

### device\_event\_ai\_interaction

`device_ai_interaction_result<native><public> := struct<epic_internal>:`

* Payload of `device_event_ai_interaction`.
* Optional agent that triggered the interaction

`Source<native><public>:?agent`

* Optional agent targeted by `Source`.

`Target<native><public>:?agent`

* Results for `MoveTo`.

`move_to_result<public> := enum:`

* The destination has been reached.

`DestinationReached`

* The destination will not be reached. See debug log in UEFN for more info.

`WillNotReachDestination`

### patchwork\_device

`patchwork_device<public> := class<concrete>(creative_device_base):`

* Base class for all Patchwork devices.
* Enables this device.

`Enable<public>():void = external {}`

* Disables this device.

`Disable<public>():void = external {}`

* Define shared settings for Patchwork devices.

`music_manager_device<public> := class<concrete><final>(patchwork_device):`

* Apply a distortion effect to Patchwork audio inputs.

`distortion_effect_device<public> := class<concrete><final>(patchwork_device):`

* Modify a setting on another Patchwork device in a regularly repeating pattern.

`lfo_modulator_device<public> := class<concrete><final>(patchwork_device):`

* Turn Patchwork note inputs into audio using instrument samples.

`instrument_player_device<public> := class<concrete><final>(patchwork_device):`

* Output Patchwork audio for players to hear.

`speaker_device<public> := class<concrete><final>(patchwork_device):`

* Create drum note patterns for Patchwork devices.

`drum_sequencer_device<public> := class<concrete><final>(patchwork_device):`

* Send events to devices based on Patchwork note inputs.

`note_trigger_device<public> := class<concrete><final>(patchwork_device):`

* Apply an echo effect to Patchwork audio inputs.

`echo_effect_device<public> := class<concrete><final>(patchwork_device):`

* Turn Patchwork note inputs into audio using drum samples.

`drum_player_device<public> := class<concrete><final>(patchwork_device):`

* Modify a setting on another Patchwork device when triggered.

`value_setter_device<public> := class<concrete><final>(patchwork_device):`

* Transpose Patchwork note inputs to follow a chord progression.

`note_progressor_device<public> := class<concrete><final>(patchwork_device):`

* Turn Patchwork note inputs into audio using customizable sound synthesis.

`omega_synthesizer_device<public> := class<concrete><final>(patchwork_device):`

* Modify a setting on another Patchwork device in steps over time.

`step_modulator_device<public> := class<concrete><final>(patchwork_device):`

* Create melodic note patterns for Patchwork devices.

`note_sequencer_device<public> := class<concrete><final>(patchwork_device):`

### player\_spawner\_device

`player_spawner_device<public> := class<concrete><final>(creative_device_base):`

* Used to spawn an `agent` on an island. Use multiple `player_spawner_device`s to spawn multiple `agent`s.
* Signaled when an `agent` is spawned from this device.
* Sends the `agent` that spawned.

`SpawnedEvent<public>:listenable(agent) = external {}`

* Enables this device.

`Enable<public>():void = external {}`

* Disables this device.

`Disable<public>():void = external {}`

### player\_reference\_device

`player_reference_device<public> := class<concrete><final>(creative_device_base):`

* Used to relay `agent` statistics to other devices and `agent`s. Can transmit statistics such as elimination count, eliminated count, or scores when certain conditions are met. Can also project a hologram of the `agent` and display text that can be altered in various positions and curvatures.
* Signaled when this device is activated.
* Sends the `agent` stored in the device.

`ActivatedEvent<public>:listenable(agent) = external {}`

* Signaled when a stat tracked by this device is updated.
* Sends the `agent` stored in the device.

`TrackedStatChangedEvent<public>:listenable(agent) = external {}`

* Signaled when the `agent` tracked by this device is updated.
* Sends the new `agent` stored in the device.

`AgentUpdatedEvent<public>:listenable(agent) = external {}`

* Signaled when the `agent` tracked by this fails to be updated.
* Sends the `agent` that attempted to be stored in this device.

`AgentUpdateFailsEvent<public>:listenable(agent) = external {}`

* Signaled when the `agent` tracked by this device is replaced.
* Sends the new `agent` stored in the device.

`AgentReplacedEvent<public>:listenable(agent) = external {}`

* Enables or Disables this device.

`Enable<public>():void = external {}` `Disable<public>():void = external {}`

* Ends the round/game.

`Activate<public>():void = external {}`

* Registers `Agent` as the `agent` being tracked by this device.

`Register<public>(Agent:agent):void = external {}`

* Clears the state of this device.

`Clear<public>():void = external {}`

* Is true when `Agent` is the player being referenced by the device.

`IsReferenced<public>(Agent:agent)<transacts><decides>:void = external {}`

* Returns the `agent` currently referenced by the device.

`GetAgent<public>():?agent = external {}`

* Returns the stat value that this device is currently tracking

`GetStatValue<public>():int = external {}`

### animated\_mesh\_device

`animated_mesh_device<public> := class<concrete><final>(creative_device_base):`

* Used to select, spawn, and configure a skeletal mesh to play a specific animation.
* Starts or resumes playback of the animation.

`Play<public>():void = external {}`

* Pauses playback of the animation.

`Pause<public>():void = external {}`

* Starts or resumes reverse playback of the animation.

`PlayReverse<public>():void = external {}`

* Used to create a customizable turret that can search for nearby targets. `automated_turret_device<public> := class<concrete><final>(creative_device_base):`
* Triggers when someone enters the activation radius while nobody else is there.
* Sends the activating `agent`. If the activator is a non-agent then `false` is returned.

`ActivatedEvent<public>:listenable(?agent) = external {}`

* Triggers when the turret is damaged.
* Sends the triggering `agent`. If the activator is a non-agent then `false` is returned.

`DamagedEvent<public>:listenable(?agent) = external {}`

* Triggers when the turret is destroyed.
* Sends the triggering `agent`. If the activator is a non-agent then `false` is returned.

`DestroyedEvent<public>:listenable(?agent) = external {}`

* Sends the `agent` that was found.

`TargetFoundEvent<public>:listenable(agent) = external {}`

* Triggers when the turret loses a target.
* Sends the `agent` that was lost.

`TargetLostEvent<public>:listenable(agent) = external {}`

* Enables or disable.

`Enable<public>():void = external {}`

`Disable<public>():void = external {}`

* Set the turret to the Default Team.
* Only usable if Possible Targets is not set to Everyone

`UseDefaultTeam<public>():void = external {}`

* Set the turret to the Wildlife & Creatures team.
* Only usable if Possible Targets is not set to Everyone

`UseTeamWildlifeAndCreatures<public>():void = external {}`

* Set the turret to the same team as the supplied `Agent`.
* Only usable if Possible Targets is not set to Everyone

`SetTeam<public>(Agent:agent):void = external {}`

* Set the supplied `Agent` as the turret's target.
* The target will only change if `Agent` is within the activation radius, has direct line-of-sight to the turret,
* is on a targetable team as determined by `Possible Targets`, and is not Down But Not Out.

`SetTarget<public>(Agent:agent):void = external {}`

### cinematic\_sequence\_device

`cinematic_sequence_device<public> := class<concrete><final>(creative_device_base):`

* Used to trigger level sequences that allow coordination of cinematic animation, transformation, and audio tracks.
* Signaled when the sequence is stopped.

`StoppedEvent<public>:listenable(tuple()) = external {}`

* Plays the sequence. This will only work when the device is set to Everyone

`Play<public>():void = external {}`

* Plays the sequence. An instigating 'Agent' is required when the device is set to anything except Everyone

`Play<public>(Agent:agent):void = external {}`

* Stops the sequence.

`Stop<public>():void = external {}`

* Stops the sequence. An instigating 'Agent' is required when the device is set to anything except Everyone

`Stop<public>(Agent:agent):void = external {}`

* Go to the end and stop the sequence.

`GoToEndAndStop<public>():void = external {}`

* Go to the end and stop the sequence. An instigating 'Agent' is required when the device is set to anything except Everyone

`GoToEndAndStop<public>(Agent:agent):void = external {}`

* Pauses the sequence.

`Pause<public>():void = external {}`

* Pauses the sequence. An instigating 'Agent' is required when the device is set to anything except Everyone

`Pause<public>(Agent:agent):void = external {}`

* Toggles between `Play` and `Stop`.

`TogglePause<public>():void = external {}`

* Toggles between `Play` and `Stop`. An instigating 'Agent' is required when the device is set to anything except Everyone

`TogglePause<public>(Agent:agent):void = external {}`

* Set the playback position (in frames) of the sequence.

`SetPlaybackFrame<public>(PlaybackFrame:int):void = external {}`

* Returns the playback position (in frames) of the sequence.

`GetPlaybackFrame<public>()<transacts>:int = external {}`

* Set the playback position (in time/seconds) of the sequence.

`SetPlaybackTime<public>(PlaybackTime:float):void = external {}`

* Returns the playback position (in time/seconds) of the sequence.

`GetPlaybackTime<public>()<transacts>:float = external {}`

* Set the playback rate of the sequence.

`SetPlayRate<public>(PlayRate:float):void = external {}`

* Returns the playback rate of the sequence.

`GetPlayRate<public>()<transacts>:float = external {}`

### gameplay\_camera\_fixed\_angle\_device

`gameplay_camera_fixed_angle_device<public> := class<concrete><final>(gameplay_camera_device):`

* Used to update the camera’s current viewpoint and rotation based on a fixed angle

`gameplay_camera_fixed_point_device<public> := class<concrete><final>(gameplay_camera_device):`

* Used to update the camera’s current viewpoint and rotation based on a fixed point.

`gameplay_camera_device<public> := class<abstract><epic_internal>(creative_device_base):`

* Used to update the camera’s current viewpoint and rotation based on current camera mode.
* Enables or Disables this device.

`Enable<public>():void = external {}`

`Disable<public>():void = external {}`

* Adds the camera to the `Agent`’s camera stack and pushes it to be the active camera.

`AddTo<public>(Agent:agent):void = external {}`

* Adds the camera to all `Agent`s camera stacks and pushes it to be the active camera.

`AddToAll<public>():void = external {}`

* Removes the camera from the `Agent`’s camera stack and pops from being the active camera replacing it with the next one in the stack.

`RemoveFrom<public>(Agent:agent):void = external {}`

* Removes the camera from all `Agent`s camera stacks and pops from being the active camera replacing it with the next one in the stack.

`RemoveFromAll<public>():void = external {}`

### gameplay\_controls\_third\_person\_device

`gameplay_controls_third_person_device<public> := class<concrete><final>(gameplay_controls_device):`

* Used to adapt the controls to the camera perspective

### gameplay\_controls\_device

`gameplay_controls_device<public> := class<abstract><epic_internal>(creative_device_base):`

* Used to update the gameplay controls scheme based on current control mode.
* Enables or disables this device.

`Enable<public>():void = external {}`

`Disable<public>():void = external {}`

* Adds the gameplay control to the `Player`’s gameplay controls stack and pushes it to be the active control.

`AddTo<public>(Agent:agent):void = external {}`

* Adds the gameplay control to all `Agent`s gameplay controls stack and pushes it to be the active control.

`AddToAll<public>():void = external {}`

* Removes the gameplay control from the `Agent`’s gameplay controls stack and pops from being the active control replacing it with the next one in the stack.

`RemoveFrom<public>(Agent:agent):void = external {}`

* Removes the gameplay control from all `Agent`s gameplay controls stack and pops from being the active control replacing it with the next one in the stack.

`RemoveFromAll<public>():void = external {}`

### class\_selector\_ui\_device

`class_selector_ui_device<public> := class<concrete><final>(creative_device_base):`

* Used to allow players to select their `Class` from a `Class Selector UI`
* Signaled when an `agent` selects a class.
* Sends the `agent` that selected a class.

`ClassSelectedEvent<public>:listenable(agent) = external {}`

* Signaled when an `agent` closes the UI.
* Sends the `agent` that closed the UI.

`UIClosedEvent<public>:listenable(agent) = external {}`

* Signaled when the UI is opened.
* Sends the `agent` that is responsible for opening the UI.

`UIOpenedEvent<public>:listenable(agent) = external {}`

* Enables or disables this device.

`Enable<public>():void = external {}` `Disable<public>():void = external {}`

* Show the _Class Selector UI_ to `Agent`.

`Show<public>(Agent:agent):void = external {}`

### post\_process\_device

`post_process_device<public> := class<concrete><final>(creative_device_base):`

* Used to apply Post Process Effects to players through the creative device rather than a Post Process Volume.
* Signaled when a blend in event has finished. Sends the `agent` that used this device.

`BlendingInCompleteEvent<public>:listenable(?agent) = external {}`

* Signaled when a blend out event has finished. Sends the `agent` that used this device.

`BlendingOutCompleteEvent<public>:listenable(?agent) = external {}`

* Enables this device only for the instigating `Agent`.

`Enable<public>(Agent:agent):void = external {}`

* Enables this device for all players.

`Enable<public>():void = external {}`

* Disables this device only for the instigating `Agent`.

`Disable<public>(Agent:agent):void = external {}`

* Disables this device for all players.

`Disable<public>():void = external {}`

* Starts blending in the post process effect to the set strength only for the instigating `Agent`.

`BlendIn<public>(Agent:agent):void = external {}`

* Starts blending in the post process effect to the set strength for all players.

`BlendInForAll<public>():void = external {}`

* Starts blending out the post process effect to 0 strength only for the instigating `Agent`.

`BlendOut<public>(Agent:agent):void = external {}`

* Starts blending out the post process effect to 0 strength for all players.

`BlendOutForAll<public>():void = external {}`

* Resets to the starting strength, ending any ongoing blending only for the instigating `Agent`.

`Reset<public>(Agent:agent):void = external {}`

* Resets to the starting strength, ending any ongoing blending for all players.

`ResetForAll<public>():void = external {}`

### map\_controller\_device

`map_controller_device<public> := class<concrete><final>(creative_device_base):`

* Used to control the behavior of the map & minimap.
* Activation for a given `agent` can occur automatically via the device's _Activate Automatically_ user option, by the `agent` entering and exiting the device's volume if using the _Activate on Trigger_ user option, or via events from other devices or verse.
* When more than one map controller is activated for a given `agent`, the one with the highest _Map Priority_ user option applies.
* Adds the map controller to the provided `Agent`'s map controller stack.
* If multiple map controllers are active for an `agent`, the one with the highest _Map Priority_ is used.

`Activate<public>(Agent:agent):void = external {}`

* Adds the map controller to all `agent`s in the experience.
* If multiple map controllers are active for an `agent`, the one with the highest Map Priority is used.

`Activate<public>():void = external {}`

* Removes the map controller from the provided `Agent`'s map controller stack.

`Deactivate<public>(Agent:agent):void = external {}`

* Removes the map controller from all `agent`s in the experience.
* The next highest priority active map controller will be used, or if none exists, the default behavior will be restored.

`Deactivate<public>():void = external {}`

* Enables the device.
* Enabling the device will allow it to be activated, both by incoming events, and by trigger if using _Activate on Trigger_.

`Enable<public>():void = external {}`

* Disables the device.
* Disabling the device will deactivate it for all `agents` in the experience, turn off the trigger functionality, and prevent it from responding to events.

`Disable<public>():void = external {}`

* Sets the Capture Box Size (in meters).
* Capture Box Size refers to the length and width of the area used for both the map capture image as well as the activation trigger.
* Value is clamped between `25.0` and `2500.0` meters.

`SetCaptureBoxSize<public>(Size:float):void = external {}`

* Returns the Capture Box Size (in meters).

`GetCaptureBoxSize<public>()<transacts>:float = external {}`

### accolades\_device

`accolades_device<public> := class<concrete><final>(creative_device_base):`

* Used to set up islands so players will earn Battle Pass XP when they interact with your island. Accolades are achievements or accomplishments that players can complete to earn XP.

`TestAwardEvent<public>:listenable(agent) = external {}`

* Signaled when testing the accolade to make sure it is awarded as expected. Only signals within unpublished island environments.
* Sends the `agent` receiving the achievement.
* Enable or Disable

`Enable<public>():void = external {}` `Disable<public>():void = external {}`

* Awards the XP to `agent`

`Award<public>(Agent:agent):void = external {}`

### analytics\_device

`analytics_device<public> := class<concrete><final>(creative_device_base):`

* Used to track `agent` events used to generate analytics.
* Enable or Disable

`Enable<public>():void = external {}` `Disable<public>():void = external {}`

* Submits an event for `Agent`

`Submit<public>(Agent:agent):void = external {}`

### campfire\_device

`campfire_device<public> := class<concrete><final>(creative_device_base):`

* Used to place a campfire in the world that an `agent` can use to heal themselves

`AgentEntersEffectAreaEvent<public>:listenable(agent) = external {}` `AgentExitsEffectAreaEvent<public>:listenable(agent) = external {}`

* Signaled when an `agent` enters or exits the area of effect for this device, Sends the entering or exiting `agent` as instigator

`CampfirePulseEvent<public>:listenable(tuple()) = external {}`

* Signaled when this device generates a pulse.

`AgentPulsedEvent<public>:listenable(agent) = external {}`

* Signaled when an `agent` is affected by a pulse generated by this device, Sends the affected `agent`

`LitEvent<public>:listenable(agent) = external {}` `ExtinguishedEvent<public>:listenable(agent) = external {}`

* Signaled when this device is lit or extinguished by an `agent` who is also the instigator

`EnabledEvent<public>:listenable(tuple()) = external {}` `DisabledEvent<public>:listenable(tuple()) = external {}`

* Signaled when this device is enabled or disabled

`AddWood<public>():void = external {}`

* Adds wood to this device.

`Light<public>(Agent:agent):void = external {}`

* Lights this device.

`Extinguish<public>(Agent:agent):void = external {}`

* Extinguishes this device.

### crowd\_volume\_device

`crowd_volume_device<public> := class<concrete><final>(creative_device_base):`

* Spawns a crowd to cheer you on.
* Enables this device.

`Enable<public>():void = external {}`

* Disables this device.

`Disable<public>():void = external {}`

### item\_remover\_device

`item_remover_device<public> := class<concrete><final>(creative_device_base):`

* Used to cause `agent`s to drop or lose items from their inventory. For example, if an `agent` is Down But Not Out, they could drop items from their inventory, and other `agent`s could then pick up those items.
* Enables this device. `Enable<public>():void = external {}`
* Disables this device. `Disable<public>():void = external {}`
* Remove items from `Agent`s inventory. The items that are removed can be configured using _Affected Items_. `Remove<public>(Agent:agent):void = external {}`

### character\_device

`character_device<public> := class<concrete>(creative_device_base):`

* Used to configure a single interactive mannequin, that can visualize characters, clothing, and perform emotes.

`InteractedWithEvent<public>:listenable(agent) = external {}`

* Signaled when an `agent` interacts with this device, Sends the `agent` that interacted with this device.

`Enable<public>():void = external {}`

* Enables this device.

`Disable<public>():void = external {}`

* Disables this device.

`Show<public>():void = external {}` `Hide<public>():void = external {}`

* Toggle visibility

`PlayEmote<public>():void = external {}`

* Plays an emote on the character created by this device.

### player\_marker\_device

`player_marker_device<public> := class<concrete><final>(creative_device_base):`

* Used to mark an `agent`'s position on the minimap and configure the information shown for marked `agent`s.

`FirstItemValueChangedEvent<public>:listenable(agent) = external {}`

* Signaled when the first item type monitored on marked agents has changed.
* Sends the marked `agent`.

`SecondItemValueChangedEvent<public>:listenable(agent) = external {}`

* Signaled when the second item type monitored on marked agents has changed.
* Sends the marked `agent`.

`FirstItemValueReachedEvent<public>:listenable(agent) = external {}`

* Signaled when a marked `agent` meets the quantity condition for the first monitored item type (e.g. Fewer Than, Equal To, More Than X).
* Sends the marked `agent`.

`SecondItemValueReachedEvent<public>:listenable(agent) = external {}`

* Signaled when a marked `agent` meets the quantity condition for the second monitored item type (e.g. Fewer Than, Equal To, More Than X).
* Sends the marked `agent`.

`Attach<public>(Agent:agent):void = external {}` `Detach<public>(Agent:agent):void = external {}`

* Attaches a marker to `Agent`.
* Detaches a marker from `Agent`.

`DetachFromAll<public>():void = external {}`

* Detaches markers from all marked `agent`s.

### player\_checkpoint\_device

`player_checkpoint_device<public> := class<concrete><final>(creative_device_base):`

* Used to set an `agent`'s spawn point when activated. This can also clear the `agent`'s inventory.

`FirstActivationEvent<public>:listenable(agent) = external {}`

* Signaled when this device is first activated by any `agent`.
* Sends the `agent` that activated this device.
* Signaled each time a new `agent` activates this device.
* Sends the `agent` that activated this device.

`FirstActivationPerAgentEvent<public>:listenable(agent) = external {}`

* Enables this device.

`Enable<public>():void = external {}`

* Disables this device.

`Disable<public>():void = external {}`

* Registers this checkpoint for `Agent`. This sets the respawn point and can clear `Agent`'s inventory depending on this device's settings. Multiple `agent`s can be registered to this device at one time.

`Register<public>(Agent:agent):void = external {}`

### real\_time\_clock\_device

`real_time_clock_device<public> := class<concrete><final>(creative_device_base):`

* Used to trigger in game events based on real world time.
* Signaled when the optional second _Duration_ time has been reached.

`DurationElapsedEvent<public>:listenable(tuple()) = external {}`

* Signaled when the target time is reached.

`TimeReachedEvent<public>:listenable(tuple()) = external {}`

* Signaled when this device is enabled after the target time has been reached.

`EnablingAfterTimeReachedEvent<public>:listenable(tuple()) = external {}`

* Signaled when this device is enabled before the target time has been reached.

`EnablingBeforeTimeReachedEvent<public>:listenable(tuple()) = external {}`

* Enables this device.

`Enable<public>():void = external {}`

* Disables this device.

`Disable<public>():void = external {}`

### prop\_mover\_device

`prop_mover_device<public> := class<concrete><final>(creative_device_base):`

* Used to move around a building or prop, and customize responses to various collision event types.

`EnabledEvent<public>:listenable(tuple()) = external {}`

* Signaled when this device is disabled.

`DisabledEvent<public>:listenable(tuple()) = external {}`

* Signaled when the prop movement begins.

`BeganEvent<public>:listenable(tuple()) = external {}`

* Signaled when the prop movement ends.

`EndedEvent<public>:listenable(tuple()) = external {}`

* Signaled when the prop reaches its destination.

`FinishedEvent<public>:listenable(tuple()) = external {}`

* Signaled when the prop changes its direction.

`MovementModeChangedEvent<public>:listenable(tuple()) = external {}`

* Signaled when the prop hits an `agent`.
* Sends the `agent` hit by the prop.

`AgentHitEvent<public>:listenable(agent) = external {}`

* Signaled when the prop hits a creature, animal, or NPC.

`AIHitEvent<public>:listenable(tuple()) = external {}`

* Signaled when the prop hits another prop.

`PropHitEvent<public>:listenable(tuple()) = external {}`

* Enables this device.

`Enable<public>():void = external {}`

* Disables this device.

`Disable<public>():void = external {}`

* Moves the prop to its original position.

`Reset<public>():void = external {}`

* Begins the prop moving.

`Begin<public>():void = external {}`

* Ends the prop moving.

`End<public>():void = external {}`

* Moves the prop forward based on this device's default configuration, ignoring the prop's previous movement.

`Advance<public>():void = external {}`

* Reverses the prop's moving direction.

`Reverse<public>():void = external {}`

* Sets the total distance (in meters) that the prop will move.

`SetTargetDistance<public>(InDistance:float):void = external {}`

* Returns the total distance (in meters) that the prop will move.

`GetTargetDistance<public>()<transacts>:float = external {}`

* Sets the speed (in meters per second) at which the prop will move to its destination. `SetTargetSpeed<public>(Speed:float):void = external {}`
* Returns the speed (in meters per second) at which the prop mover will move the prop to its destination. `GetTargetSpeed<public>()<transacts>:float = external {}`

### switch\_device

`switch_device<public> := class<concrete><final>(creative_device_base):`

* Used to allow agents to turn other linked devices on/off or other custom state changes.
* Signaled when the switch is turned on by the specified `agent`.
* Sends the `agent` that turned on the device. `TurnedOnEvent<public>:listenable(agent) = external {}`
* Signaled when the switch is turned off by the specified `agent`.
* Sends the `agent` that turned off the device. `TurnedOffEvent<public>:listenable(agent) = external {}`
* Signaled if the switch is on when the state is checked. `IfOnWhenCheckedEvent<public>:listenable(tuple()) = external {}`
* Signaled if the switch is off when the state is checked. `IfOffWhenCheckedEvent<public>:listenable(tuple()) = external {}`
* Signaled when the switch state is saved. `StateSaveEvent<public>:listenable(tuple()) = external {}`
* Signaled when the switch state changes. `StateChangesEvent<public>:listenable(tuple()) = external {}`
* Signaled when the switch state is loaded by the specified `agent`.
* Sends the `agent` that loaded the state on the device. `StateLoadEvent<public>:listenable(agent) = external {}`
* Signaled when the persistent data is cleared by the specified `agent`.
* Sends the `agent` that cleared persistent data on the device. `ClearEvent<public>:listenable(agent) = external {}`
* Enables this device. `Enable<public>():void = external {}`
* Disables this device. `Disable<public>():void = external {}`
* Turns on this device with `Agent` acting as the instigator of the action. `TurnOn<public>(Agent:agent):void = external {}`
* Turns off the device with `Agent` acting as the instigator of the action. `TurnOff<public>(Agent:agent):void = external {}`
* Toggles between `TurnOn` and `TurnOff` with `Agent` acting as the instigator of the action. `ToggleState<public>(Agent:agent):void = external {}`
* Loads the device state with `Agent` acting as the instigator of the action. `LoadState<public>(Agent:agent):void = external {}`
* Saves the device state with `Agent` acting as the instigator of the action. `SaveState<public>(Agent:agent):void = external {}`
* Loads the device state for all players. `LoadStateForAll<public>():void = external {}`
* Saves the device state for all players `SaveStateForAll<public>():void = external {}`
* Checks the device state with `Agent` acting as the instigator of the action. `CheckState<public>(Agent:agent):void = external {}`
* Clears persistence data for `Agent`. `ClearPersistenceData<public>(Agent:agent):void = external {}`
* Clears persistence data for all `agent`s. `ClearAllPersistenceData<public>():void = external {}`
* Returns the current state of this switch: true (on) or false (off). Use this overload of `GetCurrentState` when this device has _Store State Per Player_ set to _Yes_. `GetCurrentState<public>(Agent:agent)<transacts><decides>:void = external {}`
* Returns the current state of this switch: true (on) or false (off). Use this overload of `GetCurrentState` when this device has _Store State Per Player_ set to _No_. `GetCurrentState<public>()<transacts><decides>:void = external {}`
* Query whether this device has a single global on/off state, or has a personalized on/off state for each individual agent. `IsStatePerAgent<public>()<transacts><decides>:void = external {}`
* Sets the _Interaction Time_ required to activate this device (in seconds). `SetInteractionTime<public>(Time:float):void = external {}`
* Returns the _Interaction Time_ required to activate this device (in seconds). `GetInteractionTime<public>()<transacts>:float = external {}`
* Sets the _Turn On Text_ to be displayed to a user when the switch is currently off, and offers an interaction to switch it on. Clamped to 150 characters. `SetTurnOnInteractionText<public>(Text:message):void = external {}`
* Sets the _Turn Off Text_ to be displayed to a user when the switch is currently on, and offers an interaction to switch it off. Clamped to 150 characters. `SetTurnOffInteractionText<public>(Text:message):void = external {}`
* Sets the state of the switch to a specific value for a specific `Agent`.
* Use when the device has _Store State Per Player_ set to _Yes_. `SetState<public>(Agent:agent, State:logic):void = external {}`
* Sets the state of the switch to a specific value.
* Use when the device has _Store State Per Player_ set to _No_. `SetState<public>(State:logic):void = external {}`
* Updates the _State Reset Time_ for the device, in seconds, clamped to the Min and Max defined in the device.
* This will not apply to any state reset timers currently in effect.
* Set to 0.0 to disable the State Reset Time. Set to less than 0.0 to reset to default. `SetStateResetTime<public>(Time:float):void = external {}`
* Updates the _State Reset Time_ for the device, in seconds,for a specific player (if _Store State Per Player_ is _Yes_), clamped to the Min and Max defined in the device.
* This will not apply to any state reset timers currently in effect.
* Set to 0.0 to disable the State Reset Time. Set to less than 0.0 to reset to default. `SetStateResetTime<public>(Agent:agent, Time:float):void = external {}`
* Returns the value of _State Reset Time_, in seconds, for the device. Returns -1.0 if _State Reset Time_ is not used. `GetStateResetTime<public>()<transacts>:float = external {}`

\*Returns the value of _State Reset Time_, in seconds, for the device, for a specific player. Returns -1.0 if _State Reset Time_ is not used. `GetStateResetTime<public>(Agent:agent)<transacts>:float = external {}`

* Returns the time, in seconds, before the switch will reset itself to default.
* Returns -1.0 if _Store State Per Player_ is _Yes_ or if there is no active reset timer. `GetCurrentResetTime<public>():float = external {}`
* Returns the time, in seconds, before the switch will reset itself to default for _Agent_.
* Returns -1.0 if there is no active reset timer. `GetCurrentResetTime<public>(Agent:agent):float = external {}`

### volume\_device

`volume_device<public> := class<concrete><final>(creative_device_base):`

* Used to track when agents enter and exit a volume.
* Signaled when an `agent` enters the device volume. `AgentEntersEvent<public>:listenable(agent) = external {}`
* Signaled when an `agent` exits the device volume. `AgentExitsEvent<public>:listenable(agent) = external {}`

### crash\_pad\_device

`crash_pad_device<public> := class<concrete><final>(creative_device_base):`

* Used to place a crash pad that can bounce players and protect them from fall damage.
* Signaled when an `agent` is launched by this device.
* Sends the launched `agent`. `LaunchedEvent<public>:listenable(agent) = external {}`
* Enables this device. `Enable<public>():void = external {}`
* Disables this device. `Disable<public>():void = external {}`

### fishing\_zone\_device

`fishing_zone_device<public> := class<concrete><final>(creative_device_base):`

* Used to add fishing mechanics to experiences, such as:
* Signaled when an `agent` catches a fish.
* Sends the `agent` that caught the fish. `CaughtEvent<public>:listenable(agent) = external {}`
* Signaled when all items have been caught and removed.
* Sends the `agent` that caught the last fish. `EmptyEvent<public>:listenable(agent) = external {}`
* Enables this device. `Enable<public>():void = external {}`
* Disables this device. `Disable<public>():void = external {}`
* Resets the number of available uses for this device back to _Uses Allowed_. `Reset<public>():void = external {}`
* Returns all caught and removed items to the inventory. This only works when _Pool Type_ is set to _Device Inventory_. `Restock<public>():void = external {}`

### hud\_controller\_device

`hud_controller_device<public> := class<concrete><final>(creative_device_base):`

* Used to show or hide parts of the HUD for players or teams.
* Use this with other devices such as the `hud_message_device`, `map_indicator_device`, and `billboard_device` to control the HUD
* Enables this device. `Enable<public>():void = external {}`
* Disables this device. `Disable<public>():void = external {}`
* Sets the _Affected Class_ option to `Agent`'s class. `UpdateAffectedClass<public>(Agent:agent):void = external {}`
* Sets the _Affected Team_ option to `Agent`'s team. `UpdateAffectedTeam<public>(Agent:agent):void = external {}`
* Resets the _Affected Class_ option to its starting value. `ResetAffectedClass<public>():void = external {}`
* Resets the _Affected Team_ option to its starting value. `ResetAffectedTeam<public>():void = external {}`

### changing\_booth\_device := class(creative\_device\_base):

`changing_booth_device<public> := class<concrete><final>(creative_device_base):`

* Allows players to change their outfit in game

### end\_game\_device

`end_game_device<public> := class<concrete><final>(creative_device_base):`

* Used to configure rules that can end the current round or game.
* Enables this device. `Enable<public>():void = external {}`
* Disables this device. `Disable<public>():void = external {}`
* Ends the round/game. Uses `Agent`'s team to determine if the round/game ends when _Activating Team_ is enabled. `Activate<public>(Agent:agent):void = external {}`

### race\_manager\_device

`race_manager_device<public> := class<concrete><final>(creative_device_base):`

* Used with the `race_checkpoint_device` to create more advanced racing modes.
* Signaled when the race begins.
* Sends the `agent` that started the race. `RaceBeganEvent<public>:listenable(agent) = external {}`
* Signaled when an `agent` finishes the race.
* Sends the `agent` that finished the race. `RaceCompletedEvent<public>:listenable(agent) = external {}`
* Signaled when an `agent` completes their first lap.
* Sends the `agent` that finished the lap. `FirstLapCompletedEvent<public>:listenable(agent) = external {}`
* Signaled when an `agent` completes a lap.
* Sends the `agent` that finished the lap. `LapCompletedEvent<public>:listenable(agent) = external {}`
* Enables this device. `Enable<public>():void = external {}`
* Disables this device. `Disable<public>():void = external {}`
* Begins the race. `Begin<public>():void = external {}`
* Ends the race. `End<public>():void = external {}`

### race\_checkpoint\_device

`race_checkpoint_device<public> := class<concrete><final>(creative_device_base):`

* Used in tandem with `race_manager_device` to define the route players must traverse.
* Signaled when this checkpoint becomes the next checkpoint that `agent`s need to pass for the first time.
* Sends the first `agent` who is now targeting this checkpoint. `CheckpointBecomesCurrentForTheFirstTimeEvent<public>:listenable(agent) = external {}`
* Signaled when this checkpoint becomes the current checkpoint for `agent`.
* Sends the `agent` who is now targeting this checkpoint. `CheckpointBecomesCurrentEvent<public>:listenable(agent) = external {}`
* Signaled when an `agent` passes this checkpoint.
* Sends the `agent` that passed this checkpoint. `CheckpointCompletedEvent<public>:listenable(agent) = external {}`
* Enables this device. `Enable<public>():void = external {}`
* Disables this device. `Disable<public>():void = external {}`
* Sets this checkpoint as the current checkpoint for `Agent`. This only functions if `Agent` has not already passed this checkpoint. `SetAsCurrentCheckpoint<public>(Agent:agent):void = external {}`

### item\_shop\_device

`item_shop_device<public> := class<concrete><final>(creative_device_base):`

* Allows the item shop to be opened when activated
* Enables this device. `Enable<public>():void = external {}`
* Disables this device. `Disable<public>():void = external {}`

### ai\_patrol\_path\_device

`ai_patrol_path_device<public> := class<concrete><final>(creative_device_base):`

* Used to create patrolling behavior for guards spawned with the `guard_spawner_device`.
* Assign an AI to this patrol path. `Assign<public>(Patroller:agent):void = external {}`
* Signaled when a guard reaches this device. `NodeReachedEvent<public>:listenable(agent) = external {}`
* Signaled when a guard cannot reach the next `ai_patrol_path_device`. `NextNodeUnreachableEvent<public>:listenable(agent) = external {}`
* Signaled when a guard starts moving on the patrol path. `PatrolPathStartedEvent<public>:listenable(agent) = external {}`
* Signaled when a guard stops moving on the patrol path. `PatrolPathStoppedEvent<public>:listenable(agent) = external {}`
* Enables this device. `Enable<public>():void = external {}`
* Disables this device. `Disable<public>():void = external {}`
* Commands patroller to follow the _Next Patrol Path Group_ instead of the default _Patrol Path Group_. `GoToNextPatrolGroup<public>(Patroller:agent):void = external {}`

### audio\_mixer\_device

`audio_mixer_device<public> := class<concrete><final>(creative_device_base):`

* Used to manage sound buses via control bus mixes set on the Audio Mixer Device.
* Activates the mix set on the audio mixer. `ActivateMix<public>():void = external {}`
* Deactivates the mix set on the audio mixer. `DeactivateMix<public>():void = external {}`
* Adds `Agent` as a target when using the _CanBeHeardBy_ Registered Players or NonRegisteredPlayers options. `Register<public>(Agent:agent):void = external {}`
* Removes `Agent` as a target when using the _CanBeHeardBy_ Registered Players or NonRegisteredPlayers options. `Unregister<public>(Agent:agent):void = external {}`
* Removes all previously registered `agent`s when using the _CanBeHeardBy_ Registered Players or NonRegisteredPlayers options. `UnregisterAll<public>():void = external {}`

### audio\_player\_device

`audio_player_device<public> := class<concrete><final>(creative_device_base):`

* Used to configure and play audio from the device location or from registered `agent`s.
* Enables this device. Allows this device to be triggered from other linked devices (i.e. triggers) and allow calls to `Play` to succeed. `Enable<public>():void = external {}`
* Disables this device. No longer allows this device to be triggered from other linked devices (i.e. triggers) and will stop any currently playing audio. `Disable<public>():void = external {}`
* Starts playing audio from this device for `Agent`. This can only be used when the device is set to be _Heard by Instigator_. `Play<public>(Agent:agent):void = external {}`
* Starts playing audio from this device. `Play<public>():void = external {}`
* Stops any audio playing from this device for `Agent`. This can only be used when the device is set to be _Heard by Instigator_. `Stop<public>(Agent:agent):void = external {}`
* Stops any audio playing from this device. `Stop<public>():void = external {}`
* Adds `Agent` as a target to play audio from when activated. `Register<public>(Agent:agent):void = external {}`
* Removes `Agent` as a target to play audio from when activated. `Unregister<public>(Agent:agent):void = external {}`
* Removes all previously registered `agent`s as valid targets to play audio from when activated. `UnregisterAll<public>():void = external {}`
* Shows this device in the world. `Show<public>()<transacts>:void = external {}`
* Hides this device from the world. `Hide<public>()<transacts>:void = external {}`

### bouncer\_device

`bouncer_device<public> := class<concrete><final>(creative_device_base):`

* Used to create a bouncer that can launch players, vehicles, and more into the air with optional effects.
* Signaled when the condition in the _On Bounced Trigger_ option is met and someone or something is launched.
* Sends the `agent` that bounced. If a vehicle bounced, sends the driver. If a projectile bounced, sends its instigator.
* Sends `false` if something else bounced, including a vehicle with no driver `BouncedEvent<public>:listenable(?agent) = external {}`
* Signaled when the heal effect starts for an `agent`. `HealStartEvent<public>:listenable(agent) = external {}`
* Signaled when the heal effect stops for an `agent`. `HealStopEvent<public>:listenable(agent) = external {}`
* Enables bouncing on this device, as well as any visual and audio effects. `Enable<public>():void = external {}`
* Disables bouncing on this device, as well as any visual and audio effects. `Disable<public>():void = external {}`

### signal\_remote\_manager\_device

`<public> := class<concrete><final>(creative_device_base):`

* Used to trigger a custom response to a _Primary_ or _Secondary_ signal, sent by a _Signal Remote_ item.
* Signaled when a player has triggered the _Primary_ signal using a _Signal Remote_ item. (Fire button)
* Sends the `agent` that triggered the signal. `PrimarySignalEvent<public>:listenable(agent) = external {}`
* Signaled when a player has triggered the _Secondary_ signal using a _Signal Remote_ item. (ADS button)
* Sends the `agent` that triggered the signal. `SecondarySignalEvent<public>:listenable(agent) = external {}`
* Enables this device. `Enable<public>():void = external {}`
* Disables this device. `Disable<public>():void = external {}`

### creature\_spawner\_device

`creature_spawner_device<public> := class<concrete><final>(creative_device_base):`

* Used to spawn one or more waves of creatures of customizable types at selected time intervals.
* Signaled when a creature is spawned.
* Sends the `agent` creature who was spawned. `SpawnedEvent<public>:listenable(agent) = external {}`
* Signaled when a creature is eliminated.
* `Source` is the `agent` that has eliminated the creature. If the creature was eliminated by a non-agent then `Source` is 'false'.
* `Target` is the creature that was eliminated. `EliminatedEvent<public>:listenable(device_ai_interaction_result) = external {}`
* Enables this device. `Enable<public>():void = external {}`
* Disables this device. `Disable<public>():void = external {}`
* Destroys this device. `DestroySpawner<public>():void = external {}`
* Eliminates all creatures spawned by this device. `EliminateCreatures<public>():void = external {}`
* Returns the spawn limit of the device. `GetSpawnLimit<public>()<transacts>:int = external {}`

### creature\_placer\_device

`creature_placer_device<public> := class<concrete><final>(creative_device_base):`

* Used to spawn a creature at a specified location.
* Signaled when a creature is spawned.
* Sends the `agent` creature who was spawned. `SpawnedEvent<public>:listenable(agent) = external {}`
* Signaled when the creature is eliminated.
* Sends the `agent` that eliminated the creature.
* Sends `false` if the creature was eliminated by something other than an `agent` e.g. a vehicle. `EliminatedEvent<public>:listenable(?agent) = external {}`
* Spawns the creature. `Spawn<public>():void = external {}`
* Despawns the creature. `Despawn<public>():void = external {}`

### creature\_manager\_device

`creature_manager_device<public> := class<concrete><final>(creative_device_base):`

* Used to customize one creature type at a time. Place multiple `creature_manager_device`s for each type of creature on your island.
* Sends the `agent` that eliminated the creature. `MatchingCreatureTypeEliminatedEvent<public>:listenable(agent) = external {}`
* Enables this device. `Enable<public>():void = external {}`
* Disables this device. `Disable<public>():void = external {}`

### elimination\_feed\_device

`elimination_feed_device<public> := class<concrete><final>(creative_device_base):`

* Used to send custom messages to the elimination feed.
* Enables this device. `Enable<public>():void = external {}`
* Disables this device. `Disable<public>():void = external {}`
* Activates this device. `Agent` is used as the instigator of the action. `Activate<public>(Agent:agent):void = external {}`
* Activates this device.
* Requires _Activated by Team / Class_ be set to `All`. `Activate<public>():void = external {}`

### down\_but\_not\_out\_device

`down_but_not_out_device<public> := class<concrete><final>(creative_device_base):`

* aka DNBO
* Used to customize (or prevent) the 'down but not out' player state between 'healthy' and 'removed from game'.
* Signaled when an `agent` is set to the `down but not out` player state.
* Sends the `agent` that was downed. `AgentDownedEvent<public>:listenable(agent) = external {}`
* Signaled when an `agent` in the `down but not out` player state is picked up.
* Sends the `agent` that was picked up. `AgentPickedUpEvent<public>:listenable(agent) = external {}`
* Signaled when an `agent` in the `down but not out` player state is dropped.
* Sends the `agent` that was dropped. `AgentDroppedEvent<public>:listenable(agent) = external {}`
* Signaled when an `agent` in the `down but not out` player state is thrown.
* Sends the `agent` that was thrown. `AgentThrownEvent<public>:listenable(agent) = external {}`
* Signaled when an `agent` in the `down but not out` player state is revived.
* Sends the `agent` that was revived. `AgentRevivedEvent<public>:listenable(agent) = external {}`
* Signaled when an `agent` is the aggressor of a shake down.
* Sends the `agent` that is the aggressor. `ShakeDownEvent<public>:listenable(agent) = external {}`
* Signaled when an `agent` is the victim of a shake down.
* Sends the `agent` that is the victim. `ShakenDownEvent<public>:listenable(agent) = external {}`
* Enables this device. `Enable<public>():void = external {}`
* Disables this device. `Disable<public>():void = external {}`
* Sets the `Agent` to the `down but not out` player state. `Down<public>(Agent:agent):void = external {}`
* Sets the `Agent` to the `healthy` player state if they are in the `down but not out` player state. `Revive<public>(Agent:agent):void = external {}`

### firefly\_spawner\_device

`firefly_spawner_device<public> := class<concrete><final>(creative_device_base):`

* Used to spawn fireflies that can be collected by `agent`s.
* Signaled when a firefly is collected.
* Sends the `agent` collected the firefly. `OnFirefliesCollected<public>:listenable(agent) = external {}`
* Enables this device. `Enable<public>():void = external {}`
* Disables this device. `Disable<public>():void = external {}`
* Spawns new fireflies. The previous fireflies will be destroyed before a new fireflies spawn. `Respawn<public>():void = external {}`
* Resets respawn count. `ResetRespawnCount<public>():void = external {}`

### input\_trigger\_device

`input_trigger_device<public> := class<concrete><final>(creative_device_base):`

* Used to listen for the player activating or releasing certain inputs.
* The input is defined by the _Input_ option.
* Players can configure the key for the input in the Creative Input Actions section of the Keyboard Settings.
* Enables this device.
* An Input Trigger will listen for inputs from players that meet the device requirements. `Enable<public>():void = external {}`
* Disables this device.
* A disabled Input Trigger will not listen for inputs and will never show on the HUD. `Disable<public>():void = external {}`
* Signaled when the tracked input is pressed by an `agent`.
* Sends the `agent` that pressed the input. `PressedEvent<public>:listenable(agent) = external {}`
* Signaled when the tracked input is released by an `agent`.
* Sends the `agent` that released the input.
* Sends the `float` duration that the input was held. `ReleasedEvent<public>:listenable(tuple(agent, float)) = external {}`
* Adds `Agent` to the registered player list.
* Registered Player Behavior determines whether registered players meet the device requirements. `Register<public>(Agent:agent):void = external {}`
* Removes `Agent` from the registered player list.
* Registered Player Behavior determines whether registered players meet the device requirements. `Unregister<public>(Agent:agent):void = external {}`
* Clears the list of registered players.
* Registered Player Behavior determines whether registered players meet the device requirements. `UnregisterAll<public>():void = external {}`
* Succeeds if `Agent` is currently holding the input. `IsHeld<public>(Agent:agent)<transacts><decides>:void = external {}`

### item\_placer\_device

`item_placer_device<public> := class<concrete><final>(creative_device_base):`

* Allows pickup items to be placed in the world..
* Enables this device. `Enable<public>():void = external {}`
* Disables this device. `Disable<public>():void = external {}`

### video\_player\_device

`video_player_device<public> := class<concrete><final>(creative_device_base):`

* Used to display curated videos onto in-game screens or player HUDs.
* Signaled when this device becomes the controlling streaming device for the `agent`. `StreamStartedEvent<public>:listenable(agent) = external {}`
* Enables this device. `Enable<public>():void = external {}`
* Disables this device. `Disable<public>():void = external {}`
* Enables collision checks on this device. `EnableCollision<public>():void = external {}`
* Disables collision checks on this device. `DisableCollision<public>():void = external {}`
* Transitions to fullscreen for `Agent`. `EnterFullScreen<public>(Agent:agent):void = external {}`
* Transitions to fullscreen for `Agent`. `ExitFullScreen<public>(Agent:agent):void = external {}`
* Hides the picture-in-picture video from `Agent`. `HidePIP<public>(Agent:agent):void = external {}`
* Transitions the picture-in-picture video to the default size for `Agent`. `MakePIPDefaultSize<public>(Agent:agent):void = external {}`
* Transitions the picture-in-picture video to full screen for `Agent`. `MakePIPFullScreen<public>(Agent:agent):void = external {}`
* Turns off all streaming devices of this type on the island. `EndForAll<public>():void = external {}`
* Restart the stream from the beginning. `Restart<public>():void = external {}`
* Seeks to the _Triggered Seek Time_. Caution: The stream will pause while the video buffers when seeking. `Seek<public>():void = external {}`
* Stops the currently playing stream and starts the custom stream with the audio only playing from this device. _Stream Priority_ will not work until control is released. `TakeControl<public>():void = external {}`
* If any streaming device has forced control of the stream, this will release it and play the highest priority stream in line. `ReleaseControl<public>():void = external {}`

### dance\_mannequin\_device

`dance_mannequin_device<public> := class<concrete><final>(creative_device_base):`

* Used to project a hologram of a character performing dance emotes.
* Enables this device. `Enable<public>():void = external {}`
* Disables this device. `Disable<public>():void = external {}`
* Activates the hologram using _Default Preset_ options. `ActivateDefaultPreset<public>():void = external {}`
* Activates the hologram using _Preset 2_ options. `ActivatePreset2<public>():void = external {}`
* Activates the hologram using _Preset 3_ options. `ActivatePreset3<public>():void = external {}`
* Activates the hologram using `Agent`'s skin and emotes. `ActivateSkinAndEmoteCapture<public>(Agent:agent):void = external {}`
* Deactivates the hologram. `DeactivateSkinAndEmoteCapture<public>():void = external {}`

### prop\_manipulator\_device

`<public> := class<concrete><final>(creative_device_base):`

* Used to manipulate the properties of one or more props in a specified area (e.g. Visibility/Destructibility).
* Signaled when props affected by this device are damaged.
* Sends the `agent` that damaged the prop. `DamagedEvent<public>:listenable(agent) = external {}`
* Signaled when props affected by this device are destroyed.
* Sends the `agent` that destroyed the prop. `DestroyedEvent<public>:listenable(agent) = external {}`
* Signaled when prop resource nodes affected by this device are harvested.
* Sends the `agent` that harvested resources from the prop. `HarvestingEvent<public>:listenable(agent) = external {}`
* Signaled when prop resource nodes affected by this device are completely depleted of energy.
* Sends the `agent` that depleted the prop's energy. `ResourceDepletionEvent<public>:listenable(agent) = external {}`
* Enables this device. `Enable<public>():void = external {}`
* Disables this device. `Disable<public>():void = external {}`
* Shows all props affected by this device. `ShowProps<public>():void = external {}`
* Hides all props affected by this device. `HideProps<public>():void = external {}`
* Empties the resources of all props affected by this device. `ExhaustResources<public>():void = external {}`
* Restocks the resources of all props affected by this device. `RestockResources<public>():void = external {}`
* Restores health of all props affected by this device. `RestoreHealth<public>():void = external {}`
* Sets the _Override Resource_ option to _Yes_. `SetResourceOverridesActive<public>():void = external {}`
* Sets the _Override Resource_ option to _No_. `DisableResourceNodeOverrides<public>():void = external {}`

### customizable\_light\_device

`customizable_light_device<public> := class<concrete><final>(creative_device_base):`

* Used to create a light which can have its color and brightness manipulated in response to in-game events.
* Enables this device. `Enable<public>():void = external {}`
* Disables this device. `Disable<public>():void = external {}`
* Resets the light to its initial state. `Reset<public>():void = external {}`
* Turns on the light. `TurnOn<public>():void = external {}`
* Turns off the light. `TurnOff<public>():void = external {}`
* Toggles between `TurnOn` and `TurnOff`. `Toggle<public>():void = external {}`
* Dims the light by _Dimming Amount_. `DimLight<public>():void = external {}`
* Brightens the light by _Dimming Amount_. `UndimLight<public>():void = external {}`

### player\_counter\_device

`player_counter_device<public> := class<concrete><final>(creative_device_base):`

* Used to track and react to how many players are in a particular area, and optionally display that information in game.
* Signaled when the player count matches _Target Player Count_. The frequency of evaluation against _Target Player Count_ can be controlled through the device settings. `CountSucceedsEvent<public>:listenable(tuple()) = external {}`
* Signaled when the player count does not match _Target Player Count_. The frequency of evaluation against _Target Player Count_ can be controlled through the device settings. `CountFailsEvent<public>:listenable(tuple()) = external {}`
* Signaled when a valid player enters the zone and is counted. The frequency of evaluation against the _Target Player Count_ can be controlled through the device settings.
* Sends the `agent` that is now being counted. `CountedEvent<public>:listenable(agent) = external {}`
* Signaled when a player is no longer counted by this device, such as when they leave the zone, leave the game, or are assigned to a different `team` or class.
* Sends the `agent` that is no longer being counted. `RemovedEvent<public>:listenable(agent) = external {}`
* Enables this device. `Enable<public>():void = external {}`
* Disables this device. `Disable<public>():void = external {}`
* Resets _Target Player Count_ to the default value defined in the device settings. If _Target Player Count_ was previously incremented or decremented, this reset immediately triggers a new comparison. `Reset<public>():void = external {}`
* Increments _Target Player Count_ by `1`. Immediately triggers a new comparison. `IncrementTargetCount<public>():void = external {}`
* Decrements _Target Player Count_ by `1`. Immediately triggers a new comparison. `DecrementTargetCount<public>():void = external {}`
* Triggers an evaluation of the current count vs _Target Player Count_, signaling `CountSucceedsEvent` or `CountFailsEvent` based on the evaluation result. `CompareToTarget<public>():void = external {}`
* Triggers `CountedEvent` for all `agent`s currently being counted. `TransmitForAllCounted<public>():void = external {}`
* Adds the player to the registered player list.
* Track Registered Players determines how registered players are counted. `Register<public>(Agent:agent):void = external {}`
* Removes the player from the registered player list.
* Track Registered Players determines how registered players are counted. `Unregister<public>(Agent:agent):void = external {}`
* Clears all players from the list of registered players.
* Track Registered Players determines how registered players are counted. `UnregisterAll<public>():void = external {}`
* Show this device in the world as an info panel showing Current + Required player counts. `ShowInfoPanel<public>():void = external {}`
* Hide this device info panel from the world. `HideInfoPanel<public>():void = external {}`
* Returns whether this device is represented in the world as an info panel showing Current + Required player counts. `IsShowingInfoPanel<public>()<transacts><decides>:void = external {}`
* Sets the number of players required for this counter to succeed. Immediately triggers a new comparison. `SetTargetCount<public>(Count:int):void = external {}`
* Returns the number of players required for this counter to succeed. `GetTargetCount<public>()<transacts>:int = external {}`
* Returns the number of players currently counted by this device `GetCount<public>()<transacts>:int = external {}`
* Is true if the device is currently succeeding in its comparison. `IsPassingTest<public>()<transacts><decides>:void = external {}`
* Is true if `Agent` is currently counted by this device. `IsCounted<public>(Agent:agent)<transacts><decides>:void = external {}`

### skydome\_device

`skydome_device<public> := class<concrete><final>(creative_device_base):`

* Controls how the sky looks, as well as giving you options for changing the sky
* Enables this device. `Enable<public>():void = external {}`
* Disables this device. `Disable<public>():void = external {}`

### sentry\_device

`sentry_device<public> := class<concrete><final>(creative_device_base):`

* Generates an AI bot that spawns in a location and usually attacks players when they come in range.
* Signaled when the sentry is alerted to an `agent`.
* Sends the `agent` who alerted the sentry. `AlertedEvent<public>:listenable(agent) = external {}`
* Signaled when the sentry exists the alert state.

`ExitsAlertEvent<public>:listenable(tuple()) = external {}`

* Signaled when the sentry enters the alert state.

`EntersAlertCooldownEvent<public>:listenable(tuple()) = external {}`

* Signaled when a sentry attacks an `agent`.
* Sends the `agent` who is being attacked.

`AttackingEvent<public>:listenable(agent) = external {}`

* Signaled when a sentry is eliminated.
* Sends the `agent` that eliminated the sentry. If the sentry was eliminated by a non-agent then `false` is returned.

`EliminatedEvent<public>:listenable(?agent) = external {}`

* Signaled when the sentry eliminates a creature.

`EliminatingACreatureEvent<public>:listenable(tuple()) = external {}`

* Signaled when a sentry eliminates an `agent`.
* Sends the `agent` who was eliminated by the sentry.

`EliminatingAgentEvent<public>:listenable(agent) = external {}`

* Enables this device. `Enable<public>():void = external {}`
* Disables this device. `Disable<public>():void = external {}`
* Spawns the sentry. `Spawn<public>():void = external {}`
* Destroys the current sentry. `DestroySentry<public>():void = external {}`
* Sets the sentry to the same team `Agent` is on. `JoinTeam<public>(Agent:agent):void = external {}`
* Resets the sentry to the original team designated in the device options. `ResetTeam<public>():void = external {}`
* Puts the sentry into the pacify state, preventing from entering the alert (attacking) state. `Pacify<public>():void = external {}`
* Puts the sentry into the alert state. `EnableAlert<public>():void = external {}`
* Sets the sentry to target `Agent`. The sentry will not target agents on the same team as the sentry. `Target<public>(Agent:agent):void = external {}`
* Resets the alert state. `ResetAlertCooldown<public>():void = external {}`

### supply\_drop\_spawner\_device

`supply_drop_spawner_device<public> := class<concrete><final>(creative_device_base):`

* Used to spawn and configure an aerial supply drop that can provide players with customized weapons/supplies.
* Signaled when the balloon on the supply crate is popped.
* Sends the `?agent` that popped the balloon. If no `agent` popped the balloon returns `false`. `BalloonPoppedEvent<public>:listenable(?agent) = external {}`
* Signaled when the supply crate is opened.
* Sends the `agent` that opened the crate. `OpenedEvent<public>:listenable(agent) = external {}`
* Signaled when the supply crate lands for the first time. `LandingEvent<public>:listenable(tuple()) = external {}`
* Spawns a supply drop provided one hasn't already spawned. _Owning Team_ is set to `Agent`'s team. `Spawn<public>(Agent:agent):void = external {}`
* Spawns a supply drop provided one hasn't already spawned. `Spawn<public>():void = external {}`
* Destroys the balloon and causes the supply crate to freefall. `DestroyBalloon<public>():void = external {}`
* Opens the supply crate, ignoring the locked or unlocked state. `Agent` acts as the instigator of the open action. `Open<public>(Agent:agent):void = external {}`
* Locks the supply crate so `agent`s cannot open it. `Lock<public>():void = external {}`
* Unlocks the supply crate so `agent`s can open it. `Unlock<public>():void = external {}`

### vfx\_creator\_device

`vfx_creator_device<public> := class<concrete><final>(creative_device_base):`

* Used to create and customize your own visual effects. This is more flexible than the `vfx_spawner_device`, which gives you a selection of pre-made visual effects to choose from but limits how much you can customize or change those effects.
* Enables this device. `Enable<public>():void = external {}`
* Disables this device. `Disable<public>():void = external {}`
* Toggles between `Enable` and `Disable`. `ToggleEnabled<public>():void = external {}`
* Starts playing the effect. `Begin<public>():void = external {}`
* Starts the effect at `Agent`'s location. This option is only valid if _Stick to Player_ is enabled. `Begin<public>(Agent:agent):void = external {}`
* Starts the effect at every `agent`'s location. This option is only valid if _Stick to Player_ is enabled. `BeginForAll<public>():void = external {}`
* Ends playing the effect. `End<public>():void = external {}`
* Ends the effect at `Agent`'s location. This option is only valid if _Stick to Player_ is enabled. `End<public>(Agent:agent):void = external {}`
* Ends the effect at every `agent`'s locations. This option is only valid if _Stick to Player_ is enabled. `EndForAll<public>():void = external {}`
* Toggles between `Begin` and `End`. `Toggle<public>():void = external {}`
* Toggles between `Begin` and `End`. `Toggle<public>(Agent:agent):void = external {}`
* Toggles between `BeginForAll` and `EndForAll`. `ToggleForAll<public>():void = external {}`
* Pauses the effect if the effect is running. If the effect is paused, unpauses the effect. Pausing an effect causes the effect to freeze in place. `TogglePause<public>():void = external {}`
* Pauses the effect at `Agent`'s locations if it is playing, or resumes the effect if it is paused.
* When paused the effect freezes in place. `TogglePause<public>(Agent:agent):void = external {}`
* Pauses the effect at every `agent`'s locations if it is playing, or resumes the effect if it is paused.
* When paused the effect freezes in place. `TogglePauseForAll<public>():void = external {}`
* Removes the effect from `Agent` and continues playing at the device location. This option is only valid if _Stick to Player_ is enabled. `Remove<public>(Agent:agent):void = external {}`
* Removes the effect for every `agent` and continues playing at the device location. This option is only valid if _Stick to Player_ is enabled. `RemoveFromAll<public>():void = external {}`
* Spawns the effect at `Agent`'s location. This option is only valid if _Stick to Player_ is enabled. `SpawnAt<public>(Agent:agent):void = external {}`

### vfx\_spawner\_device

`vfx_spawner_device<public> := class<concrete><final>(creative_device_base):`

* Used to place visual effects around your island. You can use these effects to enhance the overall theme and experience of your game.
* Signaled when the effect is enabled. `EffectEnabledEvent<public>:listenable(tuple()) = external {}`
* Signaled when the effect is disabled. `EffectDisabledEvent<public>:listenable(tuple()) = external {}`
* Enables this device. `Enable<public>():void = external {}`
* Disables this device. `Disable<public>():void = external {}`
* Restarts the VFX. Triggers the VFX if it's Burst VFX. `Restart<public>():void = external {}`

### water\_device

`water_device<public> := class<concrete><final>(creative_device_base):`

* Used to create and manipulate volumes of water where players can swim, fish, or drive boats.
* Signaled when an `agent` enters the water.
* Sends `agent` that entered the water. `AgentEntersWaterEvent<public>:listenable(agent) = external {}`
* Signaled when an `agent` exits the water.
* Sends `agent` that exited the water. `AgentExitsWaterEvent<public>:listenable(agent) = external {}`
* Signals when the volume is filled to the water level set in the `Default Vertical Water Percentage` option. `VerticalFillingCompletedEvent<public>:listenable(tuple()) = external {}`
* Signals when the water volume is completely empty. `VerticalEmptyingCompletedEvent<public>:listenable(tuple()) = external {}`
* Enables this device. `Enable<public>():void = external {}`
* Disables this device. `Disable<public>():void = external {}`
* Resets the water level in the volume to the value set in the _Default Vertical Water Percentage_ option. `Reset<public>():void = external {}`
* Starts vertically emptying the water in the volume. `BeginVerticalEmptying<public>():void = external {}`
* Starts vertically filling the water in the volume. `BeginVerticalFilling<public>():void = external {}`
* Stops filling or emptying the volume. `StopVerticalMovement<public>():void = external {}`
* Resumes either filling or emptying the volume. `ResumeVerticalMovement<public>():void = external {}`

### skydive\_volume\_device

`skydive_volume_device<public> := class<concrete><final>(effect_volume_device):`

* Used to create a zone where players are put into a skydive state.
* Signaled when an `agent` enters the volume.
* Sends the `agent` that entered the volume. `AgentEntersEvent<public>:listenable(agent) = external {}`
* Signaled when an `agent` exits the volume.
* Sends the `agent` that exited the volume. `AgentExitsEvent<public>:listenable(agent) = external {}`
* Signaled when the zone changes from empty to occupied.
* Sends the `agent` that entered the volume. `ZoneOccupiedEvent<public>:listenable(agent) = external {}`
* Signaled when the zone changes from occupied to empty.
* Sends the `agent` that last left the volume. `ZoneEmptiedEvent<public>:listenable(agent) = external {}`
* Enables volume locking which prevents users from leaving the volume once they've entered. `EnableVolumeLocking<public>():void = external {}`
* Disables volume locking which prevents users from leaving the volume once they've entered. `DisableVolumeLocking<public>():void = external {}`
* Is true when `Agent` is in the volume. `IsInVolume<public>(Agent:agent)<transacts><decides>:void = external {}`

### mutator\_zone\_device

`mutator_zone_device<public> := class<concrete><final>(effect_volume_device):`

* Used to specify a zone where custom gameplay effects can be applied (e.g. gravity, no build, no weapons).
* Signaled when an `agent` in this zone begins emoting. This will not signal if the `agent` is on the _Safe Team_ or if _Affects Players_ is disabled.
* Sends the `agent` that started emoting. `AgentBeginsEmotingEvent<public>:listenable(agent) = external {}`
* Signaled when an `agent` in this zone ends emoting. This will not signal if the `agent` is on the _Safe Team_ or if _Affects Players_ is disabled.
* Sends the `agent` that stopped emoting. `AgentEndsEmotingEvent<public>:listenable(agent) = external {}`
* Signaled when an `agent` enters this zone.
* Sends the `agent` entering this zone. `AgentEntersEvent<public>:listenable(agent) = external {}`
* Signaled when an `agent` exits this zone.
* Sends the `agent` exiting this zone. `AgentExitsEvent<public>:listenable(agent) = external {}`
* Updates `Selected Class` to `Agent`'s class. `UpdateSelectedClass<public>(Agent:agent):void = external {}`
* Updates `Selected Team` to `Agent`'s team. `UpdateSelectedTeam<public>(Agent:agent):void = external {}`
* Is true when `Agent` is in the zone. `IsInVolume<public>(Agent:agent)<transacts><decides>:void = external {}`

### fire\_volume\_device

`fire_volume_device<public> := class<concrete><final>(effect_volume_device):`

* Used to specify an area which allows (or prevents) various objects, terrain, or buildings from being set on fire.
* Extinguishes objects inside this device area. `Extinguish<public>():void = external {}`
* Ignites objects inside this device area. `Ignite<public>():void = external {}`

### effect\_volume\_device

`effect_volume_device<public> := class<abstract><epic_internal>(creative_device_base):`

* Base class for types of volumes with special gameplay properties.
* Enables this device. `Enable<public>():void = external {}`
* Disables this device. `Disable<public>():void = external {}`

### damage\_volume\_device

`damage_volume_device<public> := class<concrete><final>(effect_volume_device):`

* Used to specify an area volume which can damage `agent`s, vehicles, and creatures.
* Signaled when an `agent` enters the volume.
* Sends the `agent` entering the volume. `AgentEntersEvent<public>:listenable(agent) = external {}`
* Signaled when an `agent` exits the volume.
* Sends the `agent` exiting the volume. `AgentExitsEvent<public>:listenable(agent) = external {}`

`UpdateSelectedClass<public>(Agent:agent):void = external {}`

`UpdateSelectedTeam<public>(Agent:agent):void = external {}`

* Sets the damage to be applied each tick within the volume. `Damage` is clamped between `1` and `500`. `SetDamage<public>(Damage:int):void = external {}`
* Returns the damage to be applied each tick within the volume. `GetDamage<public>()<transacts>:int = external {}`
* Is true when `Agent` is in the zone. `IsInVolume<public>(Agent:agent)<transacts><decides>:void = external {}`

### barrier\_device

`barrier_device<public> := class<concrete><final>(creative_device_base):`

* Creates an impenetrable zone that can block `agent` movement and weapon fire.
* Enables this device. `Enable<public>():void = external {}`
* Disables this device. `Disable<public>():void = external {}`
* Adds the specified `agent` to a list of additional `agent`s that the Barrier should ignore. This list is in addition to the Ignore Team and Ignore Class options. Note: Has no effect on bullets. `AddToIgnoreList<public>(Agent:agent):void = external {}`
* Removes the specified `agent` from the ignore list. The `agent` will still be ignored if they are on an ignored team or of an ignored class. `RemoveFromIgnoreList<public>(Agent:agent):void = external {}`
* Removes all `agent`s from the ignore list. `Agent`s will still be ignored if they are on an ignored team or of an ignored class. `RemoveAllFromIgnoreList<public>():void = external {}`

### visual\_effect\_powerup\_device

`visual_effect_powerup_device<public> := class<concrete><final>(powerup_device):`

* Used to trigger a visual effect (a glow or an outline) when `agent`s pick it up. `using {/UnrealEngine.com/Temporary/SpatialMath}`

### vending\_machine\_device

`vending_machine_device<public> := class<concrete><final>(creative_device_base):`

* Holds and spawns items, with an optional cost for each item. Can hold up to three items, and `agent`s can cycle between these by hitting the machine with their pickaxe.
* Signaled when an item is spawned from this device.
* Sends the `agent` that used this device. `ItemSpawnedEvent<public>:listenable(agent) = external {}`
* Enables this device. `Enable<public>():void = external {}`
* Disables this device. `Disable<public>():void = external {}`
* Cycles the screen to show the next item. `CycleToNextItem<public>():void = external {}`
* Spawns an item. `SpawnItem<public>():void = external {}`

### trigger\_device

`trigger_device<public> := class<concrete><final>(trigger_base_device):`

* Used to relay events to other linked devices.
* Signaled when an `agent` triggers this device.
* Sends the `agent` that used this device. Returns `false` if no `agent` triggered the action (ex: it was triggered through code). `TriggeredEvent<public>:listenable(?agent) = external {}`
* Triggers this device with `Agent` being passed as the `agent` that triggered the action. Use an `agent` reference when this device is setup to require one for instance, you want to trigger the device only with a particular `agent`. `Trigger<public>(Agent:agent):void = external {}`
* Triggers this device, causing it to activate its `TriggeredEvent` event. `Trigger<public>():void = external {}`

### trigger\_base\_device

`trigger_base_device<public> := class<abstract><epic_internal>(creative_device_base):`

* Base class for various specialized trigger devices. See also: \* `trigger_device` \* `perception_trigger_device` \* `attribute_evaluator_device`
* Enables this device. `Enable<public>():void = external {}`
* Disables this device. `Disable<public>():void = external {}`
* Resets the number of times this device has been activated. This will set `GetTriggerCountRemaining` back to `0` `Reset<public>():void = external {}`
* Sets max times device can be triggered
* `0` can be used to indicate no limit on trigger count.
* `MaxCount` is clamped between \[0,20]. `SetMaxTriggerCount<public>(MaxCount:int):void = external {}`
* Gets the maximum amount of times this device can trigger.
* `0` indicates no limit on trigger count. `GetMaxTriggerCount<public>()<transacts>:int = external {}`
* Returns the number of times that this device can still be triggered before hitting `GetMaxTriggerCount`.
* Returns `0` if `GetMaxTriggerCount` is unlimited. `GetTriggerCountRemaining<public>()<transacts>:int = external {}`
* Sets the time (in seconds) after triggering, before the device can be triggered again if `MaxTrigger` count allows. `SetResetDelay<public>(Time:float):void = external {}`
* Gets the time (in seconds) before the device can be triggered again if `MaxTrigger` count allows. `GetResetDelay<public>()<transacts>:float = external {}`
* Sets the time (in seconds) which must pass after triggering, before this device informs other external devices that it has been triggered. `SetTransmitDelay<public>(Time:float):void = external {}`
* Gets the time (in seconds) which must pass after triggering, before this device informs other external devices that it has been triggered. `GetTransmitDelay<public>()<transacts>:float = external {}`

### trick\_tile\_device

`trick_tile_device<public> := class<concrete><final>(creative_device_base):`

* A trap device that destroys the tile it's placed on when activated.
* Signaled when the tile this device is attached to is removed. This may occur later than `TriggeredEvent` if _Activation Delay_ is set on the device.
* Sends the `agent` that activated this device. `ActivatedEvent<public>:listenable(agent) = external {}`
* Signaled when this device is triggered.
* Sends the `agent` that triggered this device. `TriggeredEvent<public>:listenable(agent) = external {}`
* Enables this device. `Enable<public>():void = external {}`
* Disables this device. While disabled this device will not react to incoming events. `Disable<public>():void = external {}`
* Flips the device between `Enabled` and `Disable`. `ToggleEnabled<public>():void = external {}`
* Restores the tile removed when this device was triggered. `Reset<public>():void = external {}`
* Enables this device to trigger when an `agent` makes contact with the device. `EnableAgentContactTrigger<public>():void = external {}`
* Disables this device from triggering when an `agent` makes contact with the device. `DisableAgentContactTrigger<public>():void = external {}`
* Flips the device between `EnableAgentContactTrigger` and `DisableAgentContactTrigger.` ToggleAgentContactTrigger():void = external {}\`
* Triggers the device, removing the associated tile. `Trigger<public>():void = external {}`
* Teleports the `trick_tile_device` to the specified `Position` and `Rotation`.
* Only the trigger will teleport, the target buildings will not change. `TeleportTo<override>(Position:vector3, Rotation:rotation)<transacts><decides>:void = external {}`
* Teleports the `trick_tile_device` to the specified location defined by `Transform`, also applies rotation and scale accordingly.
* Only the trigger will teleport, the target buildings will not change. `TeleportTo<override>(Transform:transform)<transacts><decides>:void = external {}`
* Moves the `trick_tile_device` to the specified `Position` and `Rotation` over the specified time, in seconds.
* Only the trigger will move, the target buildings will not change. `MoveTo<override>(Position:vector3, Rotation:rotation, OverTime:float)<suspends>:move_to_result = external {}`
* Moves the `trick_tile_device` to the specified `Transform` over the specified time, in seconds.
* Only the trigger will move, the target buildings will not change. `MoveTo<override>(Transform:transform, OverTime:float)<suspends>:move_to_result = external {}`

### tracker\_device

`tracker_device<public> := class<concrete><final>(creative_device_base):`

* Allows creation and HUD tracking of custom objectives for `agent`s to complete.
* Resets the progress for `Agent` and any `agent`s sharing progress. `Reset<public>(Agent:agent):void = external {}`
* Signaled when the tracked value reaches `GetTarget` for an `agent`.
* Sends the `agent` that reached `GetTarget` for their tracked value. `CompleteEvent<public>:listenable(agent) = external {}`
* Assigns the device to `Agent` (and any `agent`s sharing progress). `Assign<public>(Agent:agent):void = external {}`
* Assigns this device to all valid `agent`s. `AssignToAll<public>():void = external {}`
* Removes this device from `Agent` and any `agent`s sharing progress. `Remove<public>(Agent:agent):void = external {}`
* Removes this device from all valid `agent`s. `RemoveFromAll<public>():void = external {}`
* The objective immediately completes. `Complete<public>(Agent:agent):void = external {}`
* Increases the tracked value by _Amount to Change on Received Signal_ for `Agent`. `Increment<public>(Agent:agent):void = external {}`
* Decrease the tracked value by _Amount to Change on Received Signal_ for `Agent`. `Decrement<public>(Agent:agent):void = external {}`
* Increases the target value for `Agent` by 1. `IncreaseTargetValue<public>(Agent:agent):void = external {}`
* Decreases the target value for `Agent` by 1. `DecreaseTargetValue<public>(Agent:agent):void = external {}`
* Saves tracked progress for `Agent`. Only valid if _Use Persistence_ is set to _Use_. `Save<public>(Agent:agent):void = external {}`
* Loads tracked progress for `Agent`. Only valid if _Use Persistence_ is set to _Use_. `Load<public>(Agent:agent):void = external {}`
* Loads tracked progress for all valid `agent`s. Only valid if _Use Persistence_ is set to _Use_. `LoadForAll<public>():void = external {}`
* Clears tracked progress for `Agent`. Only valid if _Use Persistence_ is set to _Use_. `ClearPersistence<public>(Agent:agent):void = external {}`
* Sets a description for the `tracker_device`, which is displayed if _Show on HUD_ is enabled.
* `Text` has a 64 character limit. `SetDescriptionText<public>(Text:message):void = external {}`
* Sets the target value that must be achieved in order for `CompleteEvent` to trigger.
* Clamped to `0 <= TargetValue <= 10000`. `SetTarget<public>(TargetValue:int):void = external {}`
* Returns the target value that must be achieved in order for `CompleteEvent` to trigger.
* Clamped to `0 <= GetTarget <= 10000`. `GetTarget<public>()<transacts>:int = external {}`
* Sets the current tracked value for the device for all active players. `SetValue<public>(Value:int):void = external {}`
* Sets the current tracked value for the device for the Team at the `TeamIndex`.
* If _Sharing_ is set to _Individual_, this will set the value for all team members.
* If _Sharing_ is set to _All_, this will set the value for all players. `SetValue<public>(TeamIndex:int, Value:int):void = external {}`
* Sets the current tracked value for the device for a specific 'Agent'.
* If _Sharing_ is set to _Team_, this will set the value for their team.
* If _Sharing_ is set to _All_, this will set the value for everyone. `SetValue<public>(Agent:agent, Value:int):void = external {}`
* Returns the current total tracked value for all players. `GetValue<public>()<transacts>:int = external {}`
* Returns the current total tracked value for the team at `TeamIndex`. `GetValue<public>(TeamIndex:int)<transacts>:int = external {}`
* Returns the current tracked value for `Agent`. `GetValue<public>(Agent:agent)<transacts>:int = external {}`
* Set HUD title
* `Text` has a 32 character limit. `SetTitleText<public>(Text:message):void = external {}`
* Is true if `Agent` currently has the quest active. `IsActive<public>(Agent:agent)<transacts><decides>:void = external {}`
* Is true if `Agent` has reached the _TargetValue_ for the tracker. `HasReachedTarget<public>(Agent:agent)<transacts><decides>:void = external {}`

### timer\_device

`timer_device<public> := class<concrete><final>(creative_device_base):`

* Provides a way to keep track of the time something has taken, either for scoreboard purposes, or to trigger actions. It can be configured in several ways, either acting as a countdown to an event that is triggered at the end, or as a stopwatch for an action that needs to be completed before a set time runs out.
* Signaled when the timer completes or ends with success.
* Sends the `agent` that activated the timer, if any. `SuccessEvent<public>:listenable(?agent) = external {}`
* Signaled when the timer completes or ends with failure.
* Sends the `agent` that activated the timer, if any. `FailureEvent<public>:listenable(?agent) = external {}`
* Signaled when the timer enters _Urgency Mode_.
* Sends the `agent` that activated the timer, if any. `StartUrgencyModeEvent<public>:listenable(?agent) = external {}`
* Enables this device for `Agent`. `Enable<public>(Agent:agent):void = external {}`
* Enables this device. `Enable<public>():void = external {}`
* Disables this device for `Agent`. While disabled this device will not receive signals. `Disable<public>(Agent:agent):void = external {}`
* Disables this device. While disabled this device will not receive signals. `Disable<public>():void = external {}`
* Resets the timer back to its base time and stops it for `Agent`. `Reset<public>(Agent:agent):void = external {}`
* Resets the timer back to its base time and stops it. `Reset<public>():void = external {}`
* Resets the timer back to its base time and stops it for all `agent`s. `ResetForAll<public>(Agent:agent):void = external {}`
* Resets the timer back to its base time and stops it for all `agent`s. `ResetForAll<public>():void = external {}`
* Starts the timer for `Agent`. `Start<public>(Agent:agent):void = external {}`
* Starts the timer. `Start<public>():void = external {}`
* Pauses the timer for `Agent`. `Pause<public>(Agent:agent):void = external {}`
* Pauses the timer. `Pause<public>():void = external {}`
* Resumes the timer for `Agent`. `Resume<public>(Agent:agent):void = external {}`
* Resumes the timer. `Resume<public>():void = external {}`
* Completes the timer for `Agent`. `Complete<public>(Agent:agent):void = external {}`
* Completes the timer. `Complete<public>():void = external {}`
* Starts the timer for all `agent`s. \`StartForAll(Agent:agent):void = external {}
* Starts the timer for all `agent`s. `StartForAll<public>():void = external {}`
* Pauses the timer for all `agent`s. `PauseForAll<public>(Agent:agent):void = external {}`
* Pauses the timer for all `agent`s. `PauseForAll<public>():void = external {}`
* Resumes the timer for all `agent`s. `ResumeForAll<public>(Agent:agent):void = external {}`
* Resumes the timer for all `agent`s. `ResumeForAll<public>():void = external {}`
* Completes the timer for all `agent`s. `CompleteForAll<public>(Agent:agent):void = external {}`
* Completes the timer for all `agent`s. `CompleteForAll<public>():void = external {}`
* Saves this device's data for `Agent`. `Save<public>(Agent:agent):void = external {}`
* Loads this device's saved data for `Agent`. `Load<public>(Agent:agent):void = external {}`
* Clears this device's saved data for `Agent`. `ClearPersistenceData<public>(Agent:agent):void = external {}`
* Clears this device's saved data for all `agent`s. `ClearPersistenceDataForAll<public>(Agent:agent):void = external {}`
* Clears this device's saved data for all `agent`s. `ClearPersistenceDataForAll<public>():void = external {}`
* Sets the remaining time (in seconds) on the timer, if active, on `Agent`. `SetActiveDuration<public>(Time:float, Agent:agent):void = external {}`
* Sets the remaining time (in seconds) on the timer, if active. Use this function if the timer is set to use the same time for all `agent`'s. `SetActiveDuration<public>(Time:float):void = external {}`
* Returns the remaining time (in seconds) on the timer for `Agent`. `GetActiveDuration<public>(Agent:agent)<transacts>:float = external {}`
* Returns the remaining time (in seconds) on the timer if it is set to be global. `GetActiveDuration<public>()<transacts>:float = external {}`
* Sets the lap time indicator for `Agent`. `SetLapTime<public>(Agent:agent):void = external {}`
* Sets the lap time indicator for all `agent`s. `SetLapTimeForAll<public>(Agent:agent):void = external {}`
* Sets the lap time indicator for all `agent`s. `SetLapTimeForAll<public>():void = external {}`
* Sets the maximum duration of the timer (in seconds). `SetMaxDuration<public>(Time:float):void = external {}`
* Returns the maximum duration of the timer (in seconds). `GetMaxDuration<public>()<transacts>:float = external {}`
* Succeeds if this device is tracking timer state for each individual `agent` independently. Fails if state is being tracked globally for all `agent`'s. `IsStatePerAgent<public>()<transacts><decides>:void = external {}`

### timed\_objective\_device

`timed_objective_device<public> := class<concrete><final>(creative_device_base):`

* Configures game modes where players can start or stop timers to advance gameplay objectives, such as Attack/Defend Bomb objectives.
* Signaled when the objective begins.
* Sends the `agent` that started the timer. `BeganEvent<public>:listenable(agent) = external {}`
* Signaled when the objective ends.
* Sends the `agent` that stopped the timer. `EndedEvent<public>:listenable(agent) = external {}`
* Signaled when the objective is paused.
* Sends the `agent` that paused the timer. `PausedEvent<public>:listenable(agent) = external {}`
* Signaled when the objective is resumed.
* Sends the `agent` that resumed the timer. `ResumedEvent<public>:listenable(agent) = external {}`
* Signaled when the objective is restarted.
* Sends the `agent` that restarted the timer. `RestartedEvent<public>:listenable(agent) = external {}`
* Signaled when the objective is completed.
* Sends the `agent` that started the timer or completed the timer by calling `Complete`. `CompletedEvent<public>:listenable(agent) = external {}`
* Enables the objective for `Agent`. `Enable<public>(Agent:agent):void = external {}`
* Disables the objective for `Agent`. `Disable<public>(Agent:agent):void = external {}`
* Makes this device visible. `Show<public>():void = external {}`
* Makes this device invisible. `Hide<public>():void = external {}`
* Starts the objective with `Agent` acting as the user the interacted this device. `Begin<public>(Agent:agent):void = external {}`
* Ends the objective with `Agent` acting as the user the interacted this device. `End<public>(Agent:agent):void = external {}`
* Pauses the objective with `Agent` acting as the user the interacted this device. `Pause<public>(Agent:agent):void = external {}`
* Resumes the objective with `Agent` acting as the user the interacted this device. `Resume<public>(Agent:agent):void = external {}`
* Restarts the objective with `Agent` acting as the user the interacted this device. `Restart<public>(Agent:agent):void = external {}`
* Completes the objective with `Agent` acting as the user the interacted this device. `Complete<public>(Agent:agent):void = external {}`

### teleporter\_device

`teleporter_device<public> := class<concrete><final>(creative_device_base):`

* Customizable rift that allows `agent`s to move instantly between locations. You can use this to move players around your island, or create multi-island experiences with teleporters that take players from one island to another.
* Signaled when an `agent` enters this device.
* Sends the `agent` that entered this device. `EnterEvent<public>:listenable(agent) = external {}`
* Signaled when an `agent` emerges from this device.
* Sends the `agent` that emerged from this device.
* TeleportedEvent:listenable(agent) = external {}\`
* Enables this device. `Enable<public>():void = external {}`
* Disables this device. `Disable<public>():void = external {}`
* Teleport `Agent` to the target group using this device. `Activate<public>(Agent:agent):void = external {}`
* When a link is activated, the current destination teleporter will be able to bring the `agent` back to this origin teleporter. Both origin and destination teleporters need to have this activated to work as expected. `ActivateLinkToTarget<public>():void = external {}`
* Deactivates any currently active Link. The current destination teleporter will no longer be able to return the agent to this origin teleporter. `DeactivateLinkToTarget<public>():void = external {}`
* Resets the currently selected destination teleporter, and selects an eligible destination. If the target is a _Teleporter Group_, this may be another randomly chosen `teleporter_device` from that group. `ResetLinkToTarget<public>():void = external {}`
* Teleport `Agent` to this device. `Teleport<public>(Agent:agent):void = external {}`

### team\_settings\_and\_inventory\_device

`team_settings_and_inventory_device<public> := class<concrete><final>(creative_device_base):`

* Provides team and inventory configurations that go beyond the choices the My Island settings provide.
* Can also be used to customize individual devices and create variations in team setup.
* Signaled when an enemy of _Team_ is eliminated by a team member.
* Sends the `agent` team member who eliminated the enemy. `EnemyEliminatedEvent<public>:listenable(agent) = external {}`
* Signaled when a member of _Team_ is eliminated.
* Sends the `agent` that was eliminated. `TeamMemberEliminatedEvent<public>:listenable(agent) = external {}`
* Signaled when a member of _Team_ is spawned. Sends the `agent` that has spawned. `TeamMemberSpawnedEvent<public>:listenable(agent) = external {}`
* Signaled when _Team_ runs out of respawns. `TeamOutOfRespawnsEvent<public>:listenable(tuple()) = external {}`
* Ends the round and _Team_ wins the round. `EndRound<public>():void = external {}`
* Is true if `Agent` is on _Team_. `IsOnTeam<public>(Agent:agent)<transacts><decides>:void = external {}`

### sword\_in\_the\_stone\_device

* Used to place the Infinity Blade on your island. When placed, the Infinity Blade becomes available to any player regardless of team affiliation. `sword_in_the_stone_device<public> := class<concrete><final>(creative_device_base):`

### storm\_controller\_device

`storm_controller_device<public> := class<abstract><epic_internal>(creative_device_base):`

* Base class for various specialized storm devices. See also: \* `basic_storm_controller_device` \* `advanced_storm_controller_device`
* Signaled when storm resizing ends. Use this with the _On Finish Behavior_ option for better controls. `PhaseEndedEvent<public>:listenable(tuple()) = external {}`
* Generates the storm. _Generate Storm On Game Start_ must be set to _No_ if you choose to use `GenerateStorm`. `GenerateStorm<public>():void = external {}`
* Destroys the storm. `DestroyStorm<public>():void = external {}`
* Teleports the `storm_controller_device` to the specified `Position` and `Rotation`.
* Existing storms will not target the new location, but newly generated storms will. `TeleportTo<override>(Position:vector3, Rotation:rotation)<transacts><decides>:void = external {}`
* Teleports the `storm_controller_device` to the specified location defined by `Transform`, also applies rotation and scale accordingly.
* Existing storms will not target the new location, but newly generated storms will. `TeleportTo<override>(Transform:transform)<transacts><decides>:void = external {}`
* Moves the `storm_controller_device` to the specified `Position` and `Rotation` over the specified time, in seconds.
* Existing storms will not target the new location, but newly generated storms will. `MoveTo<override>(Position:vector3, Rotation:rotation, OverTime:float)<suspends>:move_to_result = external {}`
* Moves the `storm_controller_device` to the specified `Transform` over the specified time, in seconds.
* Existing storms will not target the new location, but newly generated storms will. `MoveTo<override>(Transform:transform, OverTime:float)<suspends>:move_to_result = external {}`

### shooting\_range\_target\_track\_device

`shooting_range_target_track_device<public> := class<concrete><final>(creative_device_base):`

* A set of customizable pop up targets that can be hit by players to trigger various events.
* Signaled when target is hit in the bullseye area. `BullseyeHitEvent<public>:listenable(tuple()) = external {}`
* Signaled when the target is hit by a player. `HitEvent<public>:listenable(tuple()) = external {}`
* Signaled when the target is hit by a player. `KnockdownEvent<public>:listenable(tuple()) = external {}`
* Signaled when the target moves up slightly, making it harder to hit. `HopUpEvent<public>:listenable(tuple()) = external {}`
* Signaled when the target moves down slightly, making it harder to hit. `HopDownEvent<public>:listenable(tuple()) = external {}`
* Signaled when the target moves from laying flat to standing upright. `PopUpEvent<public>:listenable(tuple()) = external {}`
* Signaled when the target moves from standing upright to laying flat. `PopDownEvent<public>:listenable(tuple()) = external {}`
* Enables this device. `Enable<public>():void = external {}`
* Disables this device. `Disable<public>():void = external {}`
* Resets the target to its initial settings. `Reset<public>():void = external {}`
* Moves an active (standing upright) target attached to the track up slightly, in an effort to make it harder to hit `HopUp<public>():void = external {}`
* Moves an active (standing upright) target attached to the track down slightly, in an effort to make it harder to hit `HopDown<public>():void = external {}`
* Causes the target attached to the track to transition from lying flat (inactive) to standing upright (active) `PopUp<public>():void = external {}`
* Causes the target attached to the track to transition from standing upright (active) to lying flat (inactive) `PopDown<public>():void = external {}`
* Enables movement on the track. This does not start the target moving, it only enables movement. `EnableTrackMovement<public>():void = external {}`
* Disables movement on the track. This prevents any movement from occurring, until track movement is enabled again. `DisableTrackMovement<public>():void = external {}`
* Activates the movement track. `ActivateTrack<public>():void = external {}`
* Deactivates the movement track. `DeactivateTrack<public>():void = external {}`
* Starts the target moving toward the end of the track. `MoveToEnd<public>():void = external {}`
* Starts the target moving toward the start of the track. `MoveToStart<public>():void = external {}`

### shooting\_range\_target\_device

`shooting_range_target_device<public> := class<concrete><final>(creative_device_base):`

* A single customizable pop up target that can be hit by `agent`s to trigger various events.
* Signaled when the target is hit in the bullseye area. `BullseyeHitEvent<public>:listenable(tuple()) = external {}`
* Signaled when the target is hit by an `agent`. `HitEvent<public>:listenable(tuple()) = external {}`
* Signaled when the target takes enough damage to get knocked down. `KnockdownEvent<public>:listenable(tuple()) = external {}`
* Signaled when the target moves up slightly, making it harder to hit. `HopUpEvent<public>:listenable(tuple()) = external {}`
* Signaled when the target moves down slightly, making it harder to hit. `HopDownEvent<public>:listenable(tuple()) = external {}`
* Signaled when the target moves from laying flat to standing upright. `PopUpEvent<public>:listenable(tuple()) = external {}`
* Signaled when the target moves from standing upright to laying flat. `PopDownEvent<public>:listenable(tuple()) = external {}`
* Enables this device. `Enable<public>():void = external {}`
* Disables this device. `Disable<public>():void = external {}`
* Resets the target to its initial settings. `Reset<public>():void = external {}`
* Moves an active (standing upright) target up slightly, in an effort to make it harder to hit. `HopUp<public>():void = external {}`
* Moves an active (standing upright) target down slightly, in an effort to make it harder to hit. `HopDown<public>():void = external {}`
* Causes a target to transition from lying flat (inactive) to standing upright (active). `PopUp<public>():void = external {}`
* Causes a target to transition from standing upright (active) to lying flat (inactive). `PopDown<public>():void = external {}`

### score\_manager\_device

`score_manager_device<public> := class<concrete><final>(creative_device_base):`

* Used to manipulate scores using in-experience triggers. If _Activating Team_ is set to a specific team, then you should use the `agent` overloads of each function. The `agent`'s team will be used to determine if that `agent` is allowed to affect the state of the device.
* Signaled when the this device reaches its maximum number of triggers as defined by _Times Can Trigger_.
* Sends the `agent` who last triggered the device. `MaxTriggersEvent<public>:listenable(agent) = external {}`
* Signaled when the this device awards points to an `agent`.
* Sends the `agent` who received the points. `ScoreOutputEvent<public>:listenable(agent) = external {}`
* Enables this device. `Enable<public>(Agent:agent):void = external {}`
* Enables this device. `Enable<public>():void = external {}`
* Disables this device. `Disable<public>(Agent:agent):void = external {}`
* Disables this device. `Disable<public>():void = external {}`
* Resets this device to its original state. `Reset<public>(Agent:agent):void = external {}`
* Resets this device to its original state. `Reset<public>():void = external {}`
* Grant points to `Agent`. `Activate<public>(Agent:agent):void = external {}`
* Grants points. `Activate<public>():void = external {}`
* Increments the score quantity to be awarded by the next activation by `1`. `Increment<public>(Agent:agent):void = external {}`
* Increments the score quantity to be awarded by the next activation by `1`. `Increment<public>():void = external {}`
* Decrements the score quantity to be awarded by the next activation by `1`. `Decrement<public>(Agent:agent):void = external {}`
* Decrements the score quantity to be awarded by the next activation by `1`. `Decrement<public>():void = external {}`
* Sets the score to be awarded by the next activation to `Value`. `SetScoreAward<public>(Value:int):void = external {}`
* Returns the score to be awarded by the next activation. `GetScoreAward<public>()<transacts>:int = external {}`
* Sets the score to be awarded by the next activation to `Agent`'s current score. `SetToAgentScore<public>(Agent:agent):void = external {}`
* Returns the current score for `Agent`. `GetCurrentScore<public>(Agent:agent)<transacts>:int = external {}`

### round\_settings\_device

`round_settings_device<public> := class<concrete><final>(creative_device_base):`

* Used to customize gameplay for any round-based game. It generally defines what happens to the`agent`'s inventory and rewards in each round.
* Signaled when a game round starts. `RoundBeginEvent<public>:listenable(tuple()) = external {}`
* Enables this device. `Enable<public>():void = external {}`
* Disables this device. `Disable<public>():void = external {}`
* Enables the ability for players to Matchmake into the Island. Only applies to published games that have matchmaking turned on in the Island settings `EnableMatchmaking<public>():void = external {}`
* Disables the ability for players to Matchmake into the Island. Only applies to published games that have matchmaking turned on in the Island settings `DisableMatchmaking<public>():void = external {}`
* Toggles between `EnableMatchmaking` and `DisableMatchmaking`. `ToggleMatchmaking<public>():void = external {}`
* Disables all end-round conditions. The round must be ended through calling `EndRound` or a creative event after this is called. `DisableEndRoundConditions<public>():void = external {}`

\*Ends the round immediately with `Agent`'s team set as the winner of the round. `EndRound<public>(Agent:agent):void = external {}`

### rng\_device

`rng_device<public> := class<concrete><final>(creative_device_base):`

* Used to generate random numbers between a minimum and maximum value. Events are signaled when numbers are generated.
* _Value Limit 1_ is the minimum value for generation.
* _Value Limit 2_ is the maximum value for generation.
* Signaled when the generated number >= _Winning Value_. `WinEvent<public>:listenable(tuple()) = external {}`
* Signaled when the generated number < _Winning Value_. `LoseEvent<public>:listenable(tuple()) = external {}`
* Signaled when the generated number = maximum. `RolledMaxEvent<public>:listenable(tuple()) = external {}`
* Signaled when the generated number = minimum. `RolledMinEvent<public>:listenable(tuple()) = external {}`
* Enables this device. `Enable<public>():void = external {}`
* Disables this device. `Disable<public>():void = external {}`
* Randomly generate a number between _Value Limit 1_ and _Value Limit 2_.
* If the number is >= _Winning Value_ then `WinEvent` is fired.
* If the number is < _Winning Value_ then `LoseEvent` is fired.
* If the number = minimum then `RolledMinEvent` is fired.
* If the number = maximum then `RolledMaxEvent` is fired.
* `Agent` is used as the Instigator of the roll event. `Activate<public>(Agent:agent):void = external {}`
* Randomly roll a number within the configured min + max value range.
* If the number is >= _Winning Value_ then `WinEvent` is fired.
* If the number is < _Winning Value_ then `LoseEvent` is fired.
* If the number = minimum then `RolledMinEvent` is fired.
* If the number = maximum then `RolledMaxEvent` is fired. `Activate<public>():void = external {}`
* Cancels the active number generation. `Cancel<public>():void = external {}`

### radio\_device

`radio_device<public> := class<concrete><final>(creative_device_base):`

* Used to play curated music from the device or one or more registered `agent`s.
* Starts playing audio from this device. `Play<public>():void = external {}`
* Stops playing audio from this device. `Stop<public>():void = external {}`
* Adds the specified agent as a target for the Radio to play audio from `Register<public>(Agent:agent):void = external {}`
* Removes the specified agent as a target for the Radio to play audio from if previously Registered `Unregister<public>(Agent:agent):void = external {}`
* Removes all previously registered agents as targets for the Radio to play audio from `UnregisterAll<public>():void = external {}`
* Shows this device in the world. `Show<public>()<transacts>:void = external {}`
* Hides this device from the world. `Hide<public>()<transacts>:void = external {}`

### pulse\_trigger\_device

`pulse_trigger_device<public> := class<concrete><final>(creative_device_base):`

* A device used to damage players who collide with it. Can also be used as a trigger to activate other devices.
* Enables this device. `Enable<public>():void = external {}`
* Disables this device. `Disable<public>():void = external {}`
* Starts the damage sequence. `Begin<public>():void = external {}`
* Stops the damage sequence. `End<public>():void = external {}`
* Resumes the damage sequence from the last position where it was stopped. `ResumeSequence<public>():void = external {}`
* Sets the damage to be applied to those hit by an active wave. Clamped between `0 <= GetDamage <= 100000`.
* Wave visuals will change to reflect whether the wave causes damage or not. `SetDamage<public>(Damage:float):void = external {}`
* Returns the damage to be applied to those hit by an active wave. Clamped between `0 <= GetDamage <= 100000`. `GetDamage<public>()<transacts>:float = external {}`
* Sets the total number of waves this sequence will complete before ending its sequence. `LoopCount = 0` indicates the sequence should continue indefinitely. `SetLoopCount<public>(LoopCount:int):void = external {}`
* Returns the total number of waves this sequence will complete before ending its sequence.
* `0` indicates the sequence will continue indefinitely. `GetLoopCount<public>()<transacts>:int = external {}`
* Sets the speed (in meters per second) at which the waves generated by this sequencer will travel. `SetWaveSpeed<public>(Speed:float):void = external {}`
* Returns the speed (in meters per second) at which the waves generated by this sequencer will travel. `GetWaveSpeed<public>()<transacts>:float = external {}`

### prop\_spawner\_base\_device

`prop_spawner_base_device<public> := class<abstract><epic_internal>(creative_device_base):`

* Base class for devices that spawn a prop object.
* Enables this device. `Enable<public>():void = external {}`
* Disables this device. `Disable<public>():void = external {}`
* Spawns the prop associated with this device. `SpawnObject<public>():void = external {}`
* Destroys all props spawned from this device. `DestroyAllSpawnedObjects<public>():void = external {}`

### prop\_o\_matic\_manager\_device

`prop_o_matic_manager_device<public> := class<concrete><final>(creative_device_base):`

* Allows customization of the Prop-o-Matic weapon functions and how the game reacts to players using it.
* Signaled when an `agent` begins entering a disguise.
* Sends the `agent` that began entering the disguise. `BeginEnteringDisguiseEvent<public>:listenable(agent) = external {}`
* Signaled when an `agent` finishes entering a disguise.
* Sends the `agent` that finished entering the disguise. `FinishEnteringDisguiseEvent<public>:listenable(agent) = external {}`
* Signaled when an `agent` exits a disguise.
* Sends the `agent` that exited the disguise. `ExitingDisguiseEvent<public>:listenable(agent) = external {}`
* Toggle Pinging props on/off. `SetPingProps<public>(On:logic):void = external {}`
* Adjust the ping time. `SetPingFrequency<public>(Time:float):void = external {}`
* Toggle showing the props remaining on the UI. `SetShowPropsRemaining<public>(On:logic):void = external {}`
* Toggle showing the prop ping cooldown. `SetShowPropPingCooldown<public>(On:logic):void = external {}`
* Manually ping all players that are currently hiding as props. `PingPlayerProps<public>():void = external {}`
* Manually ping a specific player if they are currently a prop. `PingPlayerProp<public>(Agent:agent):void = external {}`
* Returns whether a player is currently hiding or not. `IsPlayerProp<public>(Agent:agent)<transacts><decides>:void = external {}`

### powerup\_device

`powerup_device<public> := class<abstract><epic_internal>(creative_device_base):`

* Base class for various powerup devices offering common events like `ItemPickedUpEvent`.
* Signaled when the powerup is picked up by an `agent`.
* Sends the `agent` that picked up the powerup. `ItemPickedUpEvent<public>:listenable(agent) = external {}`
* Spawns the powerup into the experience so users can interact with it. `Spawn<public>():void = external {}`
* Despawns this powerup from the experience. `Despawn<public>():void = external {}`
* Updates the _Duration_ for this powerup, clamped to the Min and Max defined in the device.
* Will not apply to any currently applied effects. `SetDuration<public>(Time:float):void = external {}`
* Returns the _Duration_ that this powerup will be active for on any player it is applied to. `GetDuration<public>()<transacts>:float = external {}`
* If the `Agent` has the effect applied to them, this will return the remaining time the effect has.
* Returns -1.0 if the effect has an infinite duration.
* Returns 0 if the `Agent` does not have the effect applied. `GetRemainingTime<public>(Agent:agent)<transacts>:float = external {}`
* Returns the `Agent` has the powerup's effect (or another of the same type) applied to them. `HasEffect<public>(Agent:agent)<transacts><decides>:void = external {}`
* Grants this powerup to `Agent`. `Pickup<public>(Agent:agent):void = external {}`
* Grants this powerup without an agent reference.
* Requires _Apply To_ set to _All Players_. `Pickup<public>():void = external {}`

### pinball\_flipper\_device

`pinball_flipper_device<public> := class<concrete><final>(creative_device_base):`

* Used to move, damage, and give scores to players that interact with it. By default, it is activated by any player touching its front face, which rotates it counterclockwise and knocks those players away from it and slightly upward.
* Signaled when this device is activated by an `agent`.
* Sends the `agent` that activated this device. `ActivatedEvent<public>:listenable(agent) = external {}`
* Enables this device. `Enable<public>():void = external {}`
* Disables this device. `Disable<public>():void = external {}`
* Causes `Agent` to activate this device. `Activate<public>(Agent:agent):void = external {}`

### pinball\_bumper\_device

`pinball_bumper_device<public> := class<concrete><final>(creative_device_base):`

* A triggered bumper that can knock players back, damage them, and award points.
* Signaled when this device is activated by an `agent`.
* Sends the `agent` that activated this device. `ActivatedEvent<public>:listenable(agent) = external {}`
* Enables this device. `Enable<public>():void = external {}`
* Disables this device. `Disable<public>():void = external {}`
* Activates this device. `Activate<public>():void = external {}`

### perception\_trigger\_device

`perception_trigger_device<public> := class<concrete><final>(trigger_base_device):`

* Specialized `trigger_base_device` that will fire output events based on line of sight between `agent`s and the device.
* Signaled when an `agent` has direct line of sight to this device.
* Sends the `agent` that has seen this device. `AgentLooksAtDeviceEvent<public>:listenable(agent) = external {}`
* Signaled when an `agent` has lost direct line of sight to this device.
* Sends the `agent` that has lost sight of this device. `AgentLooksAwayFromDeviceEvent<public>:listenable(agent) = external {}`
* Signaled when this device has direct line of sight to an `agent`.
* Sends the `agent` seen by this device. `DeviceSeesAgentEvent<public>:listenable(agent) = external {}`
* Signaled when this device loses direct line of sight to an `agent`.
* Sends the `agent` this device has lost sight of. `DeviceLosesSightOfAgentEvent<public>:listenable(agent) = external {}`

### objective\_device

`objective_device<public> := class<concrete><final>(creative_device_base):`

* Provides a collection of destructible devices that you can select from to use as objectives in your game.
* Signaled when this device has been destroyed by an `agent`.
* Sends the `agent` that destroyed this device. `DestroyedEvent<public>:listenable(agent) = external {}`
* Shows this device in the world. `Show<public>():void = external {}`
* Hides this device from the world. `Hide<public>():void = external {}`
* Activates an objective pulse at `Agent`'s location pointing toward this device. `ActivateObjectivePulse<public>(Agent:agent):void = external {}`
* Deactivates the objective pulse at `Agent`'s location. `DeactivateObjectivePulse<public>(Agent:agent):void = external {}`
* Destroys the objective item. This is done regardless of the visibility or health of the item. `Destroy<public>(Agent:agent):void = external {}`

### movement\_modulator\_device

`movement_modulator_device<public> := class<concrete><final>(creative_device_base):`

* Used to temporarily modify the speed of `agent`s and vehicles.
* Signaled when this device is activated by an `agent`.
* Sends the `agent` that activated this device. `ActivationEvent<public>:listenable(agent) = external {}`
* Enables this device. `Enable<public>():void = external {}`
* Disables this device. `Disable<public>():void = external {}`
* Activates this device's movement effect on `Agent`. `Activate<public>(Agent:agent):void = external {}`

### matchmaking\_portal\_device

`matchmaking_portal_device<public> := class<concrete><final>(creative_device_base):`

* Used to take players to different islands and to link experiences together.
* Enables this device. `Enable<public>():void = external {}`
* Disables this device. `Disable<public>():void = external {}`

### map\_indicator\_device

`map_indicator_device<public> := class<concrete><final>(creative_device_base):`

* Used to create custom points of interest and markers on the minimap and overview map.
* Enables this device. `Enable<public>():void = external {}`
* Disables this device. `Disable<public>():void = external {}`
* Activates an objective pulse at `Agent`'s location pointing toward this device. `ActivateObjectivePulse<public>(Agent:agent):void = external {}`
* Deactivates the objective pulse at `Agent`'s location. `DeactivateObjectivePulse<public>(Agent:agent):void = external {}`

### lock\_device

`lock_device<public> := class<concrete><final>(creative_device_base):`

* Used to customize the state and accessibility of doors. `lock_device` only works with assets that have a door attached.
* Locks the door. `Agent` is the instigator of the action. `Lock<public>(Agent:agent):void = external {}`
* Unlocks the door. `Agent` is the instigator of the action. `Unlock<public>(Agent:agent):void = external {}`
* Toggles between `Lock` and `Unlock`. `Agent` is the instigator of the action. `ToggleLocked<public>(Agent:agent):void = external {}`
* Opens the door. `Agent` is the instigator of the action. `Open<public>(Agent:agent):void = external {}`
* Closes the door. `Agent` is the instigator of the action. `Close<public>(Agent:agent):void = external {}`
* Toggles between `Open` and `Close`. `Agent` is the instigator of the action. `ToggleOpened<public>(Agent:agent):void = external {}`

### item\_spawner\_device

`item_spawner_device<public> := class<concrete><final>(base_item_spawner_device):`

* Used to configuration and spawn items that players can pick up and use.
* Cycles device to next configured item. `CycleToNextItem<public>():void = external {}`

> * Spawns the current item. `SpawnItem<public>():void = external {}`

* Sets device _Respawn Item on Timer_ option (see `SetTimeBetweenSpawns`) `SetEnableRespawnTimer<public>(Respawn:logic):void = external {}`
* Returns device _Respawn Item on Timer_ option (see `SetTimeBetweenSpawns`) `GetEnableRespawnTimer<public>()<transacts>:logic = external {}`
* Sets the _Time Between Spawns_ (in seconds) after an item is collected before the next is spawned, if this device has _Respawn Item on Timer_ enabled (see `SetEnableRespawnTimer`) `SetTimeBetweenSpawns<public>(Time:float):void = external {}`
* Returns the _Time Between Spawns_ (in seconds) after an item is collected before the next is spawned, if this device has _Respawn Item on Timer_ enabled (see `SetEnableRespawnTimer`) `GetTimeBetweenSpawns<public>()<transacts>:float = external {}`

### item\_granter\_device

`item_granter_device<public> := class<concrete><final>(creative_device_base):`

* Used to grant items to `agent`s. Items can either be dropped at the `agent`'s location or added directly to their inventory.
* Signaled when an item is granted to an `agent`.
* Sends the `agent` that was granted the item. `ItemGrantedEvent<public>:listenable(agent) = external {}`
* Enables this device. `Enable<public>():void = external {}`
* Disables this device. `Disable<public>():void = external {}`
* Clears saved data for `Agent`, preventing them from receiving items while offline. This only works when _Grant While Offline_ is set to _Yes_. `ClearSaveData<public>(Agent:agent):void = external {}`
* Cycles to the next item. If _Grant on Cycle_ is set `Agent` will be granted the item. `CycleToNextItem<public>(Agent:agent):void = external {}`
* Cycles to the previous item. If _Grant on Cycle_ is set `Agent` will be granted the item. `CycleToPreviousItem<public>(Agent:agent):void = external {}`
* Cycles to a random item. If _Grant on Cycle_ is set `Agent` will be granted the item. `CycleToRandomItem<public>(Agent:agent):void = external {}`
* Grants an item to `Agent`. `GrantItem<public>(Agent:agent):void = external {}`
* Restocks this device back to its starting inventory count. `RestockItems<public>():void = external {}`
* Sets the next item to be granted.
* `Index` should be between `0` and the available item count - 1.
* Calling `SetNextItem` with an invalid index will do nothing. `SetNextItem<public>(Index:int):void = external {}`

### hud\_message\_device

`hud_message_device<public> := class<concrete><final>(creative_device_base):`

* Used to show custom HUD messages to one or more `agent`s.
* Use this when the device is setup to target specific `agent`s. `Show<public>(Agent:agent):void = external {}`
* Shows the currently set _Message_ HUD message on screen. Will replace any previously active message. `Show<public>():void = external {}`
* Hides the HUD message. `Hide<public>():void = external {}`
* Displays a Custom message to a specific _Agent_ that you define.Setting _DisplayTime_ to `0.0` will display the HUD message persistently.If not defined, or less than `0.0` the message will show for the time set on the device. `Show<public>(Agent:agent, Message:message, ?DisplayTime:float = external {}):void = external {}`
* Displays a Custom message that you define for all PlayersSetting _DisplayTime_ to `0.0` will display the HUD message persistently.If not defined, or less than `0.0` the message will show for the time set on the device. `Show<public>(Message:message, ?DisplayTime:float = external {}):void = external {}`
* Sets the time (in seconds) the HUD message will be displayed. `0.0` will display the HUD message persistently. `SetDisplayTime<public>(Time:float):void = external {}`
* Returns the time (in seconds) for which the HUD message will be displayed. `0.0` means the message is displayed persistently. `GetDisplayTime<public>()<transacts>:float = external {}`
* Sets the _Message_ to be displayed when the HUD message is activated. `Text` is clamped to 150 characters. `SetText<public>(Text:message):void = external {}`

### holoscreen\_device

`holoscreen_device<public> := class<concrete><final>(creative_device_base):`

* Used to create a holographic screen that displays a clock or other curated images.

### grind\_powerup\_device

`grind_powerup_device<public> := class<concrete><final>(powerup_device):`

* Used to let `agent`s slide on any surface with accompanying visual and audio effects.

### fuel\_pump\_device

`fuel_pump_device<public> := class<concrete><final>(creative_device_base):`

* Used to provide fuel sources for vehicles. Can also be used to deal considerable damage to `agent`s and the environment when destroyed.
* Signaled when the fuel pump is emptied.
* Sends the `agent` that emptied the fuel pump. `EmptyEvent<public>:listenable(agent) = external {}`
* Enables this device. `Enable<public>():void = external {}`
* Disables this device. `Disable<public>():void = external {}`
* Resets fuel stock to _Fuel Capacity_ value. `Reset<public>():void = external {}`
* Grants fuel to `Agent`. `Empty<public>(Agent:agent):void = external {}`

### explosive\_device

`explosive_device<public> := class<concrete><final>(creative_device_base):`

* Hazard which deals damage in a radius around it when destroyed or triggered.
* Signaled when this device explodes.
* Sends the `agent` that caused the explosion. `ExplodedEvent<public>:listenable(agent) = external {}`
* Shows this device in the world. `Show<public>():void = external {}`
* Hides this device from the world. `Hide<public>():void = external {}`
* Resets this device. `Reset<public>():void = external {}`
* Triggers this device to explode. Passes `Agent` as the instigator of the explosion. `Explode<public>(Agent:agent):void = external {}`

### experience\_settings\_device

`experience_settings_device<public> := class<concrete><final>(creative_device_base):`

* Used to customize high level properties of the game mode.

### elimination\_manager\_device

`elimination_manager_device<public> := class<concrete><final>(base_item_spawner_device):`

* Used to spawn items when an `agent` or specified target is eliminated.
* Signaled when a qualifying elimination occurs.
* Sends the eliminated `agent`. `EliminatedEvent<public>:listenable(agent) = external {}`
* Signaled when a qualifying elimination occurs.
* Sends the eliminator `agent`. If the eliminator is a non-agent then `false` is returned. `EliminationEvent<public>:listenable(?agent) = external {}`

### damage\_amplifier\_powerup\_device

`damage_amplifier_powerup_device<public> := class<concrete><final>(powerup_device):`

* Used to amplify an `agent`'s damage temporarily. This applies to any weapon the `agent` is using at the time of the powerup.
* Sets the _Magnitude_ for this powerup, clamped to the Min and Max defined in the device.
* Will not apply to any currently applied effects.
* For the Damage Amplifier Powerup, this is the damage multiplier. `SetMagnitude<public>(Magnitude:float):void = external {}`
* Returns the current _Magnitude_ for the powerup.
* For the Damage Amplifier Powerup, this is the damage multiplier. `GetMagnitude<public>()<transacts>:float = external {}`

### conditional\_button\_device

`conditional_button_device<public> := class<concrete><final>(creative_device_base):`

* Used to create a specialized button which can only be activated when `agent`s are carrying specific items.
* Signaled when this device is activated.
* Sends the `agent` that activated this device. `ActivatedEvent<public>:listenable(agent) = external {}`
* Signaled when this device fails to activate because `agent` didn't have the required items.
* Sends the `agent` that attempted to activate the device. `NotEnoughItemsEvent<public>:listenable(agent) = external {}`
* Enables this device. `Enable<public>():void = external {}`
* Disables this device. `Disable<public>():void = external {}`
* Resets this device to its original settings. `Reset<public>():void = external {}`
* Activates this device. `Agent` is used as the instigator of the action. `Activate<public>(Agent:agent):void = external {}`
* Toggles the conditional button state. `Agent` is used as the instigator of the action. `Toggle<public>(Agent:agent):void = external {}`
* Sets the text that appears when `agent`s approach the device. `Text` is limited to `150` characters and will revert back to default if empty. `SetInteractionText<public>(Text:message):void = external {}`
* Sets the time (in seconds) that an interaction with this device should take to complete. `SetInteractionTime<public>(Time:float):void = external {}`
* Returns the time (in seconds) that an interaction with this device will take to complete. `GetInteractionTime<public>()<transacts>:float = external {}`
* Sets the quantity of a specific key item type that needs to be collected in order to activate the switch.
* `KeyItemIndex` ranges from `0` to number of key item types - 1. `SetItemCountRequired<public>(KeyItemIndex:int, Count:int):void = external {}`
* Returns the total quantity of a specific key item type that needs to be collected in order to activate the switch. `GetItemCountRequired<public>(KeyItemIndex:int)<transacts>:int = external {}`
* Returns the remaining quantity of a specific key item type that needs to be collected in order to activate the switch. `GetRemainingItemCountRequired<public>(KeyItemIndex:int)<transacts>:int = external {}`
* Sets the score to be awarded for a key item. `KeyItemIndex` ranges from `0` to number of key item types - 1. `SetItemScore<public>(KeyItemIndex:int, Score:int):void = external {}`
* Returns the score to be awarded for a key item. `GetItemScore<public>(KeyItemIndex:int)<transacts>:int = external {}`
* Returns how many items an `Agent` has of the item stored at `KeyItemIndex`. `GetItemCount<public>(Agent:agent, KeyItemIndex:int):int = external {}`
* Returns if the `Agent` has all of the items required to interact with this Device. `HasAllItems<public>(Agent:agent)<transacts><decides>:void = external {}`
* Returns if the `Agent` is currently holding any of the items stored in the Device. `IsHoldingItem<public>(Agent:agent)<transacts><decides>:void = external {}`
* Returns if the `Agent` is currently holding the item stored at `KeyItemIndex`. `IsHoldingItem<public>(Agent:agent, KeyItemIndex:int)<transacts><decides>:void = external {}`

### color\_changing\_tiles\_device

`color_changing_tiles_device<public> := class<concrete><final>(creative_device_base):`

* Used to create a tile that changes colors when `agent`s interact with it.
* Signaled when this device changes color.
* Sends the `agent` that interacted with this device. `ActivatedEvent<public>:listenable(agent) = external {}`
* Enables this device. `Enable<public>():void = external {}`
* Disables this device. `Disable<public>():void = external {}`
* Shows this device in the world. `Show<public>():void = external {}`
* Hides this device from the world. `Hide<public>():void = external {}`
* Resets this device to its initial settings. `Reset<public>():void = external {}`
* Sets the color of the tile to `Agent`'s team color. `SetTeam<public>(Agent:agent):void = external {}`

### collectible\_object\_device

`collectible_object_device<public> := class<concrete><final>(creative_device_base):`

* Used to place a collectible item into the world.
* Signaled when the collectible item is collected.
* Sends the `agent` that collected the item. `CollectedEvent<public>:listenable(agent) = external {}`
* Makes the collectible visible. `Show<public>():void = external {}`
* Makes the collectible invisible. `Hide<public>():void = external {}`
* Immediately respawns the object for the instigating agent.
* This will be affected by the option _Consume If Collected By_. `Respawn<public>(Agent:agent):void = external {}`
* Immediately respawns the object for all agents. `RespawnForAll<public>():void = external {}`

### class\_designer\_device

* Used together with `class_selector_device` to create class based gameplay. Defines custom class attributes and inventory loadouts. `class_designer_device<public> := class<concrete><final>(creative_device_base):`

### class\_and\_team\_selector\_device

`class_and_team_selector_device<public> := class<concrete><final>(creative_device_base):`

* Used together with `class_designer_device` to control how/when created classes can be accessed by `agent`s.
* Signaled when an `agent` changes class.
* Sends the `agent` whose class changed. `ClassSwitchedEvent<public>:listenable(agent) = external {}`
* Signaled when an `agent` changes teams.
* Sends the `agent` whose team changed. `TeamSwitchedEvent<public>:listenable(agent) = external {}`
* Enables this device. `Enable<public>():void = external {}`
* Disables this device. `Disable<public>():void = external {}`
* Changes the `Agent`'s class. `ChangeClass<public>(Agent:agent):void = external {}`
* Changes the `Agent`'s team. `ChangeTeam<public>(Agent:agent):void = external {}`
* Changes the `Agent`'s team and class. `ChangeTeamAndClass<public>(Agent:agent):void = external {}`
* Changes the selecting team. `ChangeSelectorTeam<public>(Agent:agent):void = external {}`

### capture\_item\_spawner\_device

`capture_item_spawner_device<public> := class<concrete><final>(creative_device_base):`

* Spawns and tracks a single item as a game objective (e.g. flag).
* Signaled when spawned item is captured.
* Sends the `agent` that captured the item. `ItemCapturedEvent<public>:listenable(agent) = external {}`
* Signaled when spawned item is picked up.
* Sends the `agent` that picked up the item. `ItemPickedUpEvent<public>:listenable(agent) = external {}`
* Signaled when spawned item is dropped.
* Sends the `agent` that dropped the item. `ItemDroppedEvent<public>:listenable(agent) = external {}`
* Signaled when spawned item is returned.
* Sends the `agent` that returned the item. `ItemReturnedEvent<public>:listenable(agent) = external {}`
* Enables this device. `Enable<public>():void = external {}`
* Disables this device. `Disable<public>():void = external {}`

### capture\_area\_device

`capture_area_device<public> := class<concrete><final>(creative_device_base):`

* Used to create a zone that can trigger effects once players enter it. Can be set up to be capturable by a team, to provide a score while held, or to require a specific item as a drop-off.
* Signaled when an `agent` enters this device area.
* Sends the `agent` that entered this device area. `AgentEntersEvent<public>:listenable(agent) = external {}`
* Signaled when an `agent` exits this device area.
* Sends the `agent` that exited this device area. `AgentExitsEvent<public>:listenable(agent) = external {}`
* Signaled when the first `agent` enters this device area.
* Sends the `agent` that entered this device area. `FirstAgentEntersEvent<public>:listenable(agent) = external {}`
* Signaled when the last `agent` exits this device area.
* Sends the `agent` that exited this device area. `LastAgentExitsEvent<public>:listenable(agent) = external {}`
* Signaled when this device is contested.
* Sends the `agent` that is contesting this device. `AreaIsContestedEvent<public>:listenable(agent) = external {}`
* Signaled when this device is scored.
* Sends the `agent` that scored this device. `AreaIsScoredEvent<public>:listenable(agent) = external {}`
* Signaled when this device control change starts.
* Sends the `agent` that is triggering this device control change. `ControlChangeStartsEvent<public>:listenable(agent) = external {}`
* Signaled when this device control changes.
* Sends the `agent` that triggered this device control change. `ControlChangeEvent<public>:listenable(agent) = external {}`
* Signaled when an item is consumed by this device.
* Sends the `agent` that provided the item to this device. `ItemIsConsumedEvent<public>:listenable(agent) = external {}`
* Signaled when an item is delivered to this device.
* Sends the `agent` that delivered the item to this device. `ItemIsDeliveredEvent<public>:listenable(agent) = external {}`
* Enables this device. `Enable<public>():void = external {}`
* Disables this device. `Disable<public>():void = external {}`
* Toggles between `Enable` and `Disable`. `ToggleEnabled<public>():void = external {}`
* Allows this device to be captured. `AllowCapture<public>():void = external {}`
* Disallows this device from being captured. `DisallowCapture<public>():void = external {}`
* Toggles between `AllowCapture` and `DisallowCapture`. `ToggleCaptureAllowed<public>():void = external {}`
* Resets control of this device for all teams. `Reset<public>():void = external {}`
* Gives control of this device to the capturing `agent`'s team. `GiveControl<public>(Agent:agent):void = external {}`
* Clears control of this device for all teams. `Neutralize<public>():void = external {}`
* Activates the objective pulse for this device. `ActivateObjectivePulse<public>():void = external {}`
* Deactivates the objective pulse for this device. `DeactivateObjectivePulse<public>():void = external {}`
* Sets the _Capture Height_ (in meters) of the capture area. `SetHeight<public>(Height:float):void = external {}`
* Returns the _Capture Height_ (in meters) of the capture area. `GetHeight<public>()<varies>:float = external {}`
* Sets the _Capture Radius_ (in meters) of the capture area. `SetRadius<public>(Radius:float):void = external {}`
* Returns the _Capture Radius_ (in meters) of the capture area. `GetRadius<public>()<varies>:float = external {}`

### button\_device

`button_device<public> := class<concrete><final>(creative_device_base):`

* Used to create a button which can trigger other devices when an agent interacts with it.
* Signaled when an `agent` successfully interacts with the button for `GetInteractionTime` seconds.
* Sends the `agent` that interacted with the button. `InteractedWithEvent<public>:listenable(agent) = external {}`
* Enables this device. `Enable<public>():void = external {}`
* Disables this device. `Disable<public>():void = external {}`
* Sets the text that displays when an `agent` is close to this button and looks at it. `Text` is limited to `64` characters. `SetInteractionText<public>(Text:message):void = external {}`
* Sets the duration of the interaction required to activate this device (in seconds). `SetInteractionTime<public>(Time:float):void = external {}`
* Returns the duration of the interaction required to activate this device (in seconds). `GetInteractionTime<public>()<transacts>:float = external {}`
* Sets the maximum amount of times this button can be interacted with before it will be disabled.
* `MaxCount` must be between `0` and `10`.
* `0` indicates no limit on trigger count. `SetMaxTriggerCount<public>(MaxCount:int):void = external {}`
* Returns the maximum amount of times this button can be interacted with before it will be disabled.
* `GetTriggerMaxCount` will be between `0` and `10`.
* `0` indicates no limit on trigger count. `GetMaxTriggerCount<public>()<transacts>:int = external {}`
* Returns the number of times that this button can still be interacted with before it will be disabled. Will return `0` if `GetMaxTriggerCount` is unlimited. `GetTriggerCountRemaining<public>()<transacts>:int = external {}`

### billboard\_device

`billboard_device<public> := class<concrete><final>(creative_device_base):`

* Used to display custom text messages on a billboard.
* Shows the billboard text. `ShowText<public>():void = external {}`
* Hides the billboard text. `HideText<public>():void = external {}`
* Updates the device display to show the current _Text_. `UpdateDisplay<public>():void = external {}`
* Sets the visibility of the device border mesh. This also determines whether the device collision is enabled. `SetShowBorder<public>(Show:logic):void = external {}`
* Returns `true` if the device border is enabled. `GetShowBorder<public>()<transacts>:logic = external {}`
* Sets the device _Text_. `SetText<public>(Text:message):void = external {}`
* Sets the _Text Size_ of the device _Text_. Clamped to range \[8, 24]. `SetTextSize<public>(Size:int):void = external {}`
* Returns the _Text Size_ of the device _Text_. `GetTextSize<public>()<transacts>:int = external {}`

### beacon\_device

`beacon_device<public> := class<concrete><final>(creative_device_base):`

* Used to show an in world visual effect and/or a HUD marker at the desired location.
* Enables this device. `Enable<public>():void = external {}`
* Disables this device. `Disable<public>():void = external {}`
* Adds the specified `agent` to a list of `agent`s that the Beacon will be shown to. This list of `agent`s is maintained separately from the Team Visibility set of `agent`s. `AddToShowList<public>(Agent:agent):void = external {}`
* Removes the specified `agent` from the show list. The `agent` will still see the Beacon if they meet the Team Visibility check. `RemoveFromShowList<public>(Agent:agent):void = external {}`
* Removes all `agent`s from the show list. `Agent`s will still see the Beacon if they meet the Team Visibility check. `RemoveAllFromShowList<public>():void = external {}`

### basic\_storm\_controller\_device

`basic_storm_controller_device<public> := class<concrete><final>(storm_controller_device):`

* A simplified storm device that provides a way to create a single-phase storm and control its basic behaviors.
* To control multiple phases of the storm see `advanced_storm_controller_device`.

### base\_item\_spawner\_device

`base_item_spawner_device<public> := class<abstract><epic_internal>(creative_device_base):`

* Base class for devices that spawn items.
* Signaled when an `agent` picks up the spawned item.
* Sends the `agent` that picked up the item. `ItemPickedUpEvent<public>:listenable(agent) = external {}`
* Enables this device. `Enable<public>():void = external {}`
* Disables this device. `Disable<public>():void = external {}`

### ball\_spawner\_device

`ball_spawner_device<public> := class<concrete><final>(creative_device_base):`

* Used to spawn various types of balls. Can be used to control HUD elements related to the spawned balls.
* Shows the floating HUD Icons to players, if these have been configured by the device. `ShowHUD<public>():void = external {}`
* Hides the floating HUD Icons from players, if these have been configured by the device. `HideHUD<public>():void = external {}`

### attribute\_evaluator\_device

`attribute_evaluator_device<public> := class<concrete><final>(trigger_base_device):`

* Evaluates attributes for `agent` when signaled from other devices. Acts as branching logic, checking whether the `agent` associated with the signal passes all of the tests setup in this device, then sends a signal on either `PassEvent` or `FailEvent`.
* Signaled when the `agent` from `EvaluateAgent` passes the requirements specified by this device.
* Sends the `agent` originally passed to this device in `EvaluateAgent`. `PassEvent<public>:listenable(agent) = external {}`
* Signaled when the `agent` from `EvaluateAgent` fails the requirements specified by this device.
* Sends the `agent` originally passed to this device in `EvaluateAgent`. `FailEvent<public>:listenable(agent) = external {}`
* Tests whether the specified agent satisfies the required conditions specified on the device (e.g. eliminations/score), and fires either the `PassEvent` or `FailEvent` accordingly. `EvaluateAgent<public>(Agent:agent):void = external {}`

### air\_vent\_device

`air_vent_device<public> := class<concrete><final>(creative_device_base):`

* Used to boost `agent`s, vehicles, and other objects upwards into the air.
* Enables this device. `Enable<public>():void = external {}`
* Disables this device. `Disable<public>():void = external {}`
* Activates this device. `Activate<public>():void = external {}`

### advanced\_storm\_controller\_device

`advanced_storm_controller_device<public> := class<concrete><final>(storm_controller_device):`

* Storm with custom phases

### advanced\_storm\_beacon\_device

`advanced_storm_beacon_device<public> := class<concrete><final>(creative_device_base):`

* Use with `advanced_storm_controller_device` to customize storm phases
* Teleports the `advanced_storm_beacon_device` to the specified `Position` and `Rotation`.
* Existing storms will not target the new location, but newly generated storms will. `TeleportTo<override>(Position:vector3, Rotation:rotation)<transacts><decides>:void = external {}`
* Teleports the `advanced_storm_beacon_device` to the specified location defined by `Transform`, also applies rotation and scale accordingly.
* Existing storms will not target the new location, but newly generated storms will. `TeleportTo<override>(Transform:transform)<transacts><decides>:void = external {}`
* Moves the `advanced_storm_beacon_device` to the specified `Position` and `Rotation` over the specified time, in seconds.
* Existing storms will not target the new location, but newly generated storms will. `MoveTo<override>(Position:vector3, Rotation:rotation, OverTime:float)<suspends>:move_to_result = external {}`
* Moves the `advanced_storm_beacon_device` to the specified `Transform` over the specified time, in seconds.
* Existing storms will not target the new location, but newly generated storms will. `MoveTo<override>(Transform:transform, OverTime:float)<suspends>:move_to_result = external {}`

### chair\_device

`chair_device<public> := class<concrete><final>(creative_device_base):`

* Creates a chair where `Agent`s can sit.
* Signaled when an `agent` sits on the Chair.
* Sends the sitting `agent`. `SeatedEvent<public>:listenable(agent) = external {}`
* Signaled when an `agent` stops sitting on the Chair.
* Sends the standing `Agent`. `ExitedEvent<public>:listenable(agent) = external {}`
* Enables the Chair. `Enable<public>():void = external {}`
* Disables the Chair. `Disable<public>():void = external {}`
* Allows any seated `agent` to leave the chair manually. `EnableExit<public>():void = external {}`
* Prevents any seated `agent` from leaving the Chair manually.
* While Exit is disabled, call Eject to force them out. `DisableExit<public>():void = external {}`
* Makes `Agent` sit on this chair if they meet the requirements. `Seat<public>(Agent:agent):void = external {}`
* Ejects any `agent` currently in the chair. `Eject<public>():void = external {}`
* Makes `Agent` exit this chair if they are currently in the chair. `Eject<public>(Agent:agent):void = external {}`
* Succeeds if `Agent` is currently in the chair . `IsSeated<public>(Agent:agent)<transacts><decides>:void = external {}`
* Succeeds if the chair is currently occupied. `IsOccupied<public>()<transacts><decides>:void = external {}`
* Returns the `agent` currently occupying the chair. `GetSeatedAgent<public>():?agent = external {}`

### popup\_dialog\_device

`popup_dialog_device<public> := class<concrete><final>(creative_device_base):`

* Used to create HUD text boxes that give players information, and allows responses to be customized to player choices.
* Signaled when _Button_ on this device is pushed by an `agent`.
* Sends the `agent` that pushed the button.
* Sends the `int` index of the button that was clicked. `RespondingButtonEvent<public>:listenable(tuple(agent, int)) = external {}`
* Signaled when this device is shown to an `agent`.
* Sends the `agent` looking at the popup. `ShownEvent<public>:listenable(agent) = external {}`
* Signaled when this device is dismissed by an `agent`.
* Sends the `agent` who dismissed the popup. `DismissedEvent<public>:listenable(agent) = external {}`
* Signaled when this device times out while an `agent` is looking at it.
* Sends the `agent` who was looking at the popup. `TimeOutEvent<public>:listenable(agent) = external {}`
* Enables this device. `Enable<public>():void = external {}`
* Disables this device. `Disable<public>():void = external {}`
* Shows the popup to `Agent`. `Show<public>(Agent:agent):void = external {}`
* Shows the popup to all `agent`s in the experience. `Show<public>():void = external {}`
* Hides the popup from `Agent`. `Hide<public>(Agent:agent):void = external {}`
* Hides the popup from all `agent`s in the experience. `Hide<public>():void = external {}`
* Sets the number of buttons this popup has.
* Button Count is not updated on active Popups. `SetButtonCount<public>(Count:int):void = external {}`
* Returns the _Button Text_ for this popup at a specified index. `GetButtonText<public>(Index:int)<transacts>:string = external {}`
* Sets the _Button Text_ for a button at a specific index on this popup.
* `Text` should be no more than `24` characters.
* If `Text` is empty the button will show _OK_ instead.
* Button 1 uses `Index` 0. `SetButtonText<public>(Text:message, Index:int):void = external {}`
* Sets the _Description_ text for this popup. `Text` should be no more than `350` characters. `SetDescriptionText<public>(Text:message):void = external {}`
* Returns the _Description_ text for this popup. `GetDescriptionText<public>()<transacts>:string = external {}`
* Sets the _Title_ text for this popup. `Text` should be no more than `32` characters. `SetTitleText<public>(Text:message):void = external {}`
* Returns the _Title_ text for this popup. `GetTitleText<public>()<transacts>:string = external {}`

### physics\_tree\_device

`physics_tree_device<public> := class<concrete><final>(physics_object_base_device):`

* Physics tree that can be chopped down, and damage players, vehicles, creatures, and structures.
* Signaled when a tree is spawned. `TreeSpawnedEvent<public>:listenable(tuple()) = external {}`
* Signaled when the log created by a tree is destroyed. `LogDestroyedEvent<public>:listenable(tuple()) = external {}`
* Signaled when the stump created by a tree is destroyed. `StumpDestroyedEvent<public>:listenable(tuple()) = external {}`
* Signaled when a tree has taken enough damage to be knocked down. `TreeKnockedDownEvent<public>:listenable(tuple()) = external {}`
* Releases the log from the tree, if there is one. `ReleaseLog<public>():void = external {}`
* Destroys the current log. `DestroyLog<public>():void = external {}`
* Destroys the current stump. `DestroyStump<public>():void = external {}`

### physics\_object\_base\_device

`physics_object_base_device<public> := class<abstract><epic_internal>(prop_spawner_base_device):`

* Base class for various physics-based gameplay elements (e.g. boulders/trees).

### physics\_boulder\_device

`physics_boulder_device<public> := class<concrete><final>(physics_object_base_device):`

* Physics boulder that can be dislodged and damage `agent`s, vehicles, creatures, and structures.
* Signaled when the balanced boulder is spawned on the base. `BalancedBoulderSpawnedEvent<public>:listenable(tuple()) = external {}`
* Signaled when the balanced boulder is destroyed. `BalancedBoulderDestroyedEvent<public>:listenable(tuple()) = external {}`
* Signaled when the base of the boulder is destroyed. `BaseDestroyedEvent<public>:listenable(tuple()) = external {}`
* Signaled when the rolling boulder is destroyed. `RollingBoulderDestroyedEvent<public>:listenable(tuple()) = external {}`
* Destroys the boulder's base. `DestroyBase<public>():void = external {}`
* Releases the boulder sitting on the base, if there is one. `ReleaseRollingBoulder<public>():void = external {}`
* Destroys the current rolling boulder. `DestroyRollingBoulder<public>():void = external {}`

### health\_powerup\_device

`health_powerup_device<public> := class<concrete><final>(powerup_device):`

* Used to regenerate an `agent`'s health and/or shields.
* Sets the _Magnitude_ for this powerup, clamped to the Min and Max defined in the device.
* Will not apply to any currently applied effects.
* For the Health Powerup, this is the amount of health or shield that the powerup will add or remove, `SetMagnitude<public>(Magnitude:float):void = external {}`
* Returns the current _Magnitude_ for the powerup.
* For the Health Powerup, this is the amount of health or shield that the powerup will add or remove, `GetMagnitude<public>()<transacts>:float = external {}`

### guard\_spawner\_device

`guard_spawner_device<public> := class<concrete><final>(creative_device_base):`

* Used to spawn guards that can patrol and attack other `agent`s.
* Signaled when a guard is spawned.
* Sends the `agent` guard who was spawned. `SpawnedEvent<public>:listenable(agent) = external {}`
* Signaled when a guard has identified an opponent.
* `Source` is the guard who is aware.
* `Target` is the agent who alerted the guard. `AlertedEvent<public>:listenable(device_ai_interaction_result) = external {}`
* Signaled when a guard has lost track of a target.
* `Source` is the guard that lost track of a target.
* `Target` is the `agent` no longer targeted by the guard. `TargetLostEvent<public>:listenable(device_ai_interaction_result) = external {}`
* Signaled when a guard becomes suspicious.
* Sends the `agent` guard who is suspicious. `SuspiciousEvent<public>:listenable(agent) = external {}`
* Signaled when a guard becomes unaware.
* Sends the `agent` guard who is unaware. `UnawareEvent<public>:listenable(agent) = external {}`
* Signaled when guard is damaged.
* `Source` is the `agent` that damaged the guard. If the guard was damaged by a non-agent then `false` is returned.
* `Target` is the guard that was damaged. `DamagedEvent<public>:listenable(device_ai_interaction_result) = external {}`
* Signaled when a guard is eliminated.
* `Source` is the `agent` that eliminated the guard. If the guard was eliminated by a non-agent then `Source` is 'false'.
* `Target` is the guard that was eliminated. `EliminatedEvent<public>:listenable(device_ai_interaction_result) = external {}`
* Signaled when a guard eliminates an agent.
* `Source` is the guard that eliminated the agent.
* `Target` is the agent that was eliminated. `EliminatingEvent<public>:listenable(device_ai_interaction_result) = external {}`
* Signaled when a guard is hired by a player.
* `Source` is the `agent` who hired the guard.
* `Target` is the guard that was hired. `HiredEvent<public>:listenable(device_ai_interaction_result) = external {}`
* Signaled when a guard is dismissed by a player.
* `Source` is the `agent` who dismissed the guard.
* `Target` is the guard that was dismissed. `DismissedEvent<public>:listenable(device_ai_interaction_result) = external {}`
* Enables this device. Guards will start to spawn. `Enable<public>():void = external {}`
* Disables this device. Guards will despawn if _Despawn Guards When Disabled_ is set. `Disable<public>():void = external {}`
* Resets the spawn count allowing spawning of a new batch of guards. `Reset<public>():void = external {}`
* Tries to spawn a guard. `Spawn<public>():void = external {}`
* Tries to spawn a guard. If _Auto Hire When Spawned_ is set to _Triggering Player_ the guard will be hired by `Instigator`. `Spawn<public>(Instigator:agent):void = external {}`
* Despawns guards. `Despawn<public>():void = external {}`
* Despawns guards. `Instigator` will be considered as the eliminator of those guards. `Despawn<public>(Instigator:agent):void = external {}`
* Hires guards to `Instigator`'s team. `Hire<public>(Instigator:agent):void = external {}`
* Dismisses all hired guards. `DismissAllHiredGuards<public>():void = external {}`
* Dismisses all hired guards that were recruited by `Instigator`. `DismissAgentHiredGuards<public>(Instigator:agent):void = external {}`
* Forces guards to attack `Target`, bypassing perception checks.
* 'ForgetTime' ranges from 0.0 to 600.0 (in seconds, default is 600.0), it is the time after which the target will be ignored if not found.
* 'ForgetDistance' ranges from 0.0 to 100000.0 (in centimeters, default is 100000.0), it is the distance at which the target will be ignored if not found. `ForceAttackTarget<public>(Target:agent, ?ForgetTime:float = external {}, ?ForgetDistance:float = external {}):void = external {}`
* Allows guards to be hired. `SetGuardsHireable<public>():void = external {}`
* Prevents guards from being hired. `SetGuardsNotHireable<public>():void = external {}`
* Returns the spawn limit of the device. `GetSpawnLimit<public>()<transacts>:int = external {}`

### wilds\_plant\_device

`wilds_plant_device<public> := class<concrete><final>(creative_device_base):`

* Used to create plants with explosive pods that players can detonate and launch.
* Triggers whenever the plant grows. `GrowEvent<public>:listenable(tuple()) = external {}`
* Triggers whenever the plant or launched projectile explodes.
* Sends the `agent` that initially launched the projectile or triggered an immediate explosion.
* Sends `false` if no `agent` is found. `ExplodeEvent<public>:listenable(?agent) = external {}`
* Triggers whenever the plant launches a projectile.
* Sends the `agent` that triggered this event.
* Sends `false` if no `agent` is found. `LaunchEvent<public>:listenable(?agent) = external {}`
* Enables the device to allow interaction and let it grow. `Enable<public>():void = external {}`
* Disables the device to prevent interaction and growth. `Disable<public>():void = external {}`
* Grows the plant if the device is enabled. If _Infinite Regrowths_ is `false`, this is limited by _Maximum Regrowths_. `Grow<public>():void = external {}`
* Detonates the plant if the device is enabled. `Explode<public>():void = external {}`
* Sets whether the plant can always regrow after launching a projectile or being destroyed. `SetInfiniteRegrowths<public>(InfiniteRegrowths:logic):void = external {}`
* Sets how many times the plant can regrow after launching a projectile or being destroyed.
* This applies across the device’s entire lifetime and is unaffected by _Enable_ and _Disable_.
* This value is clamped. `SetMaximumRegrowths<public>(MaximumRegrowths:int):void = external {}`

### vine\_rail\_device

`vine_rail_device<public> := class<concrete><final>(creative_device_base):`

`using {/Verse.org/Colors}`

* Used to create a customizable vine version of the Grind Rails.
* Enables this device, letting players grind on the vines. `Enable<public>():void = external {}`
* Disables this device, preventing players from grinding on the vines. `Disable<public>():void = external {}`
* Hides the track. Players can still grind on the track if it is enabled. `Hide<public>():void = external {}`
* Make this track visible. `Show<public>():void = external {}`
* Signaled when an `agent` starts grinding on this `vine_rail_device`. `StartedGrindingEvent<public>:listenable(agent) = external {}`
* Signaled when an `agent` starts grinding on this `vine_rail_device`. `EndedGrindingEvent<public>:listenable(agent) = external {}`

### grind\_rail\_device

`grind_rail_device<public> := class<concrete><final>(creative_device_base):`

* Used to create customizable Grind Rails.
* Enables this device, letting players grind on the rail. `Enable<public>():void = external {}`
* Disables this device, preventing players from grinding on the rail. `Disable<public>():void = external {}`
* Sets the color of the Grind Rail. `SetRailColor<public>(Color:color):void = external {}`
* Hides the track. Players can still grind on the track if it is enabled. `Hide<public>():void = external {}`
* Make this track visible. `Show<public>():void = external {}`
* Signaled when an `agent` starts grinding on this `grind_rail_device`. `StartedGrindingEvent<public>:listenable(agent) = external {}`
* Signaled when an `agent` starts grinding on this `grind_rail_device`. `EndedGrindingEvent<public>:listenable(agent) = external {}`

### wildlife\_spawner\_device

`wildlife_spawner_device<public> := class<concrete><final>(creative_device_base):`

* Used to spawn various wildlife that players can herd, hunt, or tame.
* Signaled when this device spawns wildlife.
* Sends the `agent` wildlife that was spawned. `SpawnedEvent<public>:listenable(agent) = external {}`
* Signaled when wildlife is eliminated.
* `Source` is the `agent` that eliminated the wildlife. If the wildlife was eliminated by a non-agent then `Source` is 'false'.
* `Target` is the wildlife that was eliminated. `EliminatedEvent<public>:listenable(device_ai_interaction_result) = external {}`
* Signaled when a wildlife eliminates an agent.
* `Source` is the wildlife that eliminated the agent.
* `Target` is the agent that was eliminated.

> `EliminatingEvent<public>:listenable(device_ai_interaction_result) = external {}`

* Signaled when wildlife is tamed.
* `Source` is the `agent` that tamed the wildlife.
* `Target` is the wildlife that was tamed. `TamedEvent<public>:listenable(device_ai_interaction_result) = external {}`
* Signaled when wildlife is untamed.
* `Source` is the `agent` that tamed the wildlife.
* `Target` is the wildlife that was untamed. `UntamedEvent<public>:listenable(device_ai_interaction_result) = external {}`
* Signaled when wildlife is force-spawned and causes the oldest wildlife to be eliminated.
* Sends the `agent` wildlife that was spawned. `ForceSpawnedEvent<public>:listenable(agent) = external {}`
* Signaled when wildlife is damaged.
* `Source` is the `agent` that damaged the wildlife. If the wildlife was damaged by a non-agent then `false` is returned.
* `Target` is the wildlife that was damaged. `DamagedEvent<public>:listenable(device_ai_interaction_result) = external {}`
* Signaled when wildlife eats a pickup such as a Shroom or Meat.
* Sends the wildlife that ate something. `SomethingIsEatenEvent<public>:listenable(agent) = external {}`
* Signaled when an `agent` rides wildlife.
* `Source` is the `agent` that started riding the wildlife.
* `Target` is the wildlife that was ridden. `RiddenEvent<public>:listenable(device_ai_interaction_result) = external {}`
* Signaled when an `agent` dismounts wildlife.
* `Source` is the `agent` that dismounted the wildlife.
* `Target` is the wildlife that was dismounted. `DismountedEvent<public>:listenable(device_ai_interaction_result) = external {}`
* Enables this device. `Enable<public>():void = external {}`
* Disables this device. `Disable<public>():void = external {}`
* Resets the count on the _Total Spawn Count_ option. `Reset<public>():void = external {}`
* Spawns wildlife from this device. `Spawn<public>():void = external {}`
* Despawns wildlife. `Agent` is marked as the one who eliminated the wildlife. `Despawn<public>(Agent:agent):void = external {}`
* Destroys this device, marking `Agent` as the destroyer of the device. `DestroySpawner<public>(Agent:agent):void = external {}`
* Tames wildlife, making them AI partners of `Agent`. `Tame<public>(Agent:agent):void = external {}`
* Untames any tamed wildlife that belong to `Agent`. `Untame<public>(Agent:agent):void = external {}`
* Untames all wildlife. `UntameAll<public>():void = external {}`
* Teleports `Agent` to the nearest wildlife, then `Agent` mounts that wildlife. `Ride<public>(Agent:agent):void = external {}`
* Dismounts `Agent` from wildlife. `Dismount<public>(Agent:agent):void = external {}`
* Dismounts all `agent`s from wildlife. `DismountAll<public>():void = external {}`
* Restores energy to wildlife belonging to `Agent` by _Energy Restore Amount_. `RestoreEnergy<public>(Agent:agent):void = external {}`
* Restores energy to wildlife by _Energy Restore Amount_. `RestoreEnergyForAll<public>():void = external {}`
* Consumes energy from wildlife belonging to `Agent` by _Energy Consume Amount_. `ConsumeEnergy<public>(Agent:agent):void = external {}`
* Consumes energy from wildlife by _Energy Consume Amount_. `ConsumeEnergyForAll<public>():void = external {}`
* Returns the spawn limit of the device. `GetSpawnLimit<public>()<transacts>:int = external {}`

### npc\_spawner\_device

`npc_spawner_device<public> := class<concrete><final>(creative_device_base):`

* Used to spawn NPCs made with Character Definition asset.
* Signaled when a character is spawned.
* Sends the `agent` character who was spawned. `SpawnedEvent<public>:listenable(agent) = external {}`
* Signaled when a character is eliminated.
* `Source` is the `agent` that eliminated the character. If the character was eliminated by a non-agent then `Source` is 'false'.
* `Target` is the character that was eliminated. `EliminatedEvent<public>:listenable(device_ai_interaction_result) = external {}`
* Enables this device. Characters will start to spawn. `Enable<public>():void = external {}`
* Disables this device. Characters will despawn if _Despawn AIs When Disabled_ is set. `Disable<public>():void = external {}`
* Resets the spawn count allowing spawning of a new batch of characters. \`Reset():void = external {}
* Tries to spawn a character. \`Spawn():void = external {}
* Despawns all characters. If set, `Instigator` will be considered as the eliminator of those characters. `DespawnAll<public>(Instigator:?agent):void = external {}`

## vehicles

### vehicle\_spawner\_device

`using {/Fortnite.com/Vehicles}`

`using {/Fortnite.com/Characters}`

`using {/Fortnite.com/Teams}`

`Vehicles<public> := module:`

`vehicle_spawner_device<public> := class<abstract><epic_internal>(creative_device_base):`

* Base class for various specialized vehicle spawners which allow specific vehicle types to be spawned and configured with specialized options.

`vehicle_spawner_sports_car_device<public> := class<concrete><final>(vehicle_spawner_device):`

* Specialized `vehicle_spawner_device` that allows a Whiplash sports car to be configured and spawned.
* Signaled when an `agent` enters the vehicle.
* Sends the `agent` that entered the vehicle. `AgentEntersVehicleEvent<public>:listenable(agent) = external {}`
* Signaled when an `agent` exits the vehicle.
* Sends the `agent` that exited the vehicle. `AgentExitsVehicleEvent<public>:listenable(agent) = external {}`
* Signaled when a vehicle is spawned or respawned by this device.
* Sends the fort\_vehicle who was spawned. `SpawnedEvent<public>:listenable(fort_vehicle) = external {}`
* Signaled when a vehicle is spawned or respawned by this device.
* Deprecated, use SpawnedEvent instead. `VehicleSpawnedEvent<public>:listenable(tuple()) = external {}`
* Signaled when a vehicle is destroyed.
* Deprecated, use DestroyedEvent instead. `VehicleDestroyedEvent<public>:listenable(tuple()) = external {}`
* Signaled when a vehicle is destroyed. `DestroyedEvent<public>:listenable(tuple()) = external {}`
* Enables this device. `Enable<public>():void = external {}`
* Disables this device. `Disable<public>():void = external {}`
* Sets `agent` as the vehicle's driver. `AssignDriver<public>(Agent:agent):void = external {}`
* Destroys the vehicle if it exists. `DestroyVehicle<public>():void = external {}`
* Spawns a new vehicle. The previous vehicle will be destroyed before a new vehicle spawns. `RespawnVehicle<public>():void = external {}`

### taxi

* Specialized `vehicle_spawner_device` that allows a taxi to be configured and spawned. `vehicle_spawner_taxi_device<public> := class<concrete><final>(vehicle_spawner_device):`

### surfboard

* Specialized `vehicle_spawner_device` that allows a surfboard to be configured and spawned. `vehicle_spawner_surfboard_device<public> := class<concrete><final>(vehicle_spawner_device):`

### shopping\_cart

* Specialized `vehicle_spawner_device` that allows a shopping cart to be configured and spawned. `vehicle_spawner_shopping_cart_device<public> := class<concrete><final>(vehicle_spawner_device):`

### quadcrasher

* Specialized `vehicle_spawner_device` that allows a Quadcrasher to be configured and spawned. `vehicle_spawner_quadcrasher_device<public> := class<concrete><final>(vehicle_spawner_device):`

### sedan

* Specialized `vehicle_spawner_device` that allows a Prevalent sedan to be configured and spawned. `vehicle_spawner_sedan_device<public> := class<concrete><final>(vehicle_spawner_device):`

### big\_rig

* Specialized `vehicle_spawner_device` that allows a Mudflap semi truck to be configured and spawned. `vehicle_spawner_big_rig_device<public> := class<concrete><final>(vehicle_spawner_device):`

### driftboard

* Specialized `vehicle_spawner_device` that allows a Driftboard to be configured and spawned. `vehicle_spawner_driftboard_device<public> := class<concrete><final>(vehicle_spawner_device):`

### cannon

* Specialized `vehicle_spawner_device` that allows a cannon to be configured and spawned. `vehicle_spawner_cannon_device<public> := class<concrete><final>(vehicle_spawner_device):`

### boat

* Specialized `vehicle_spawner_device` that allows a boat to be configured and spawned. `vehicle_spawner_boat_device<public> := class<concrete><final>(vehicle_spawner_device):`

### biplane

* Specialized `vehicle_spawner_device` that allows a Stormwing biplane to be configured and spawned. `vehicle_spawner_biplane_device<public> := class<concrete><final>(vehicle_spawner_device):`

### baller

`vehicle_spawner_baller_device<public> := class<concrete><final>(vehicle_spawner_device):`

* Specialized `vehicle_spawner_device` that allows a Baller vehicle to be configured and spawned.
* Signaled when the vehicle runs out of energy. `OutOfEnergyEvent<public>:listenable(tuple()) = external {}`
* Refills the vehicle's energy. `RefillEnergy<public>():void = external {}`

### atk

* Specialized `vehicle_spawner_device` that allows an ATK (all terrain kart) to be configured and spawned. `vehicle_spawner_atk_device<public> := class<concrete><final>(vehicle_spawner_device):`

### octane

* Spawns a lightweight vehicle made for defying gravity with its rocket boosting, jumping, and aerial maneuverability capabilities. `vehicle_spawner_octane_device<public> := class<concrete><final>(vehicle_spawner_device):`

### helicopter

* Specialized `vehicle_spawner_device` that allows a helicopter to be configured and spawned. `vehicle_spawner_helicopter_device<public> := class<concrete><final>(vehicle_spawner_device):`

### heavy turret

* Specialized `vehicle_spawner_device` that allows an anti-vehicle turret to be configured and spawned. `vehicle_spawner_heavy_turret_device<public> := class<concrete><final>(vehicle_spawner_device):`

### siege\_cannon

* Specialized `vehicle_spawner_device` that allows a siege cannon to be configured and spawned. `vehicle_spawner_siege_cannon_device<public> := class<concrete><final>(vehicle_spawner_device):`

### ufo

* Specialized `vehicle_spawner_device` that allows a UFO to be configured and spawned. `vehicle_spawner_ufo_device<public> := class<concrete><final>(vehicle_spawner_device):`

### tank

* Specialized `vehicle_spawner_device` that allows a tank to be configured and spawned. `vehicle_spawner_tank_device<public> := class<concrete><final>(vehicle_spawner_device):`

### battle\_bus

* Specialized `vehicle_spawner_device` that allows an armored battle bus to be configured and spawned.

`vehicle_spawner_armored_battle_bus_device<public> := class<concrete><final>(vehicle_spawner_device):`

### dirtbike

* Specialized `vehicle_spawner_device` that allows a dirtbike to be configured and spawned.

`vehicle_spawner_dirtbike_device<public> := class<concrete><final>(vehicle_spawner_device):`

### nitro\_drifter

* Specialized `vehicle_spawner_device` that allows a Nitro Drifter sedan to be configured and spawned.

`vehicle_spawner_nitro_drifter_sedan_device<public> := class<concrete><final>(vehicle_spawner_device):`

### sportbike

* Specialized `vehicle_spawner_device` that allows a sportbike to be configured and spawned.

`vehicle_spawner_sportbike_device<public> := class<concrete><final>(vehicle_spawner_device):`

### GetAway\_car

* Specialized `vehicle_spawner_device` that allows a GetAway Car to be configured and spawned.

`vehicle_spawner_getaway_device<public> := class<concrete><final>(vehicle_spawner_device):`

* Returns the `fort_vehicle` for `InCharacter`.
* Fails if `InCharacter` is not associated with a `fort_vehicle`.

`(InCharacter:fort_character).GetVehicle<native><public>()<transacts><decides>:fort_vehicle`

* Main API implemented by Fortnite vehicles.

`fort_vehicle<native><public> := interface<unique><epic_internal>(positional, healthful, damageable, game_action_causer):`

### IsOnGround

* Succeeds if this `fort_vehicle` is standing on ground. `IsOnGround<public>()<transacts><decides>:void`

### IsInAir

* Succeeds if this `fort_vehicle` is standing in air. `IsInAir<public>()<transacts><decides>:void`

### IsInWater

* Succeeds if this `fort_vehicle` is standing in water. `IsInWater<public>()<transacts><decides>:void`

### GepPassengers

* Returns an array with all the passengers of the vehicle. `GetPassengers<public>():[]fort_character`

## Teams

* Module import path: /Fortnite.com/Teams

`Teams<public> := module:`

* A generic set of team attitudes. Use this enum to model relationship behavior between your experience's agents/teams.

`team_attitude<native><public> := enum:`

* Agents/teams are friends. In Fortnite games two `agent`s on the same `team` are `friendly`.
* Use `fort_playspace.GetTeamCollection()` to get the `team_collection` for the active experience.

### fort\_team\_collection

`fort_team_collection<native><public> := interface<epic_internal>:`

* Collection used to manage `team`s and `agent`s on those teams.

### GetTeams

* Returns an array of all the `team`s known to this `fort_team_collection` `GetTeams<public>()<transacts>:[]team`

### AddToTeam

* Adds `InAgent` to `InTeam`.
* Fails if `InTeam` is not part of the `fort_team_collection`.

`AddToTeam<public>(InAgent:agent, InTeam:team)<transacts><decides>:void`

### IsOnTeam

* Succeeds if `InAgent` is on `InTeam`.
* Fails if:
* `InAgent` is not on `InTeam`.
* `InTeam` is not part of the `fort_team_collection`.

`IsOnTeam<public>(InAgent:agent, InTeam:team)<transacts><decides>:void`

### GetAgents

* Returns an array of all `agent`s on `InTeam`.
* Fails if `InTeam` is not part of the `fort_team_collection`.

`GetAgents<public>(InTeam:team)<transacts><decides>:[]agent`

### GetTeam

* Get the `team` that `InAgent` is on.
* Fails if `InAgent` is not on a team in this `fort_team_collection`.

`GetTeam<public>(InAgent:agent)<transacts><decides>:team`

### GetTeamAttitude

* Returns the `team_attitude` between `Team1` and `Team2`.
* Fails if:
* `Team1` is not in this `fort_team_collection`.
* `Team2` is not in this `fort_team_collection`.

`GetTeamAttitude<public>(Team1:team, Team2:team)<transacts><decides>:team_attitude`

* Returns the `team_attitude` between `Agent1` and `Agent2`.
* Fails if:
* `Agent1` is not on a team in this `fort_team_collection`.
* `Agent2` is not on a team in this `fort_team_collection`.

`GetTeamAttitude<public>(Agent1:agent, Agent2:agent)<transacts><decides>:team_attitude`

## Playspaces

* Module import path: /Fortnite.com/Playspaces

`Playspaces<public> := module:`

* A nested container that scopes objects, style, gameplay rules, visuals, etc.
* All objects and players in an experience will belong to a `fort_playspace`. There is typically one `fort_playspace` for an entire experience, though this may change in the future as the platform evolves.
* To access the `fort_playspace` for a `creative_device` use `creative_device.GetPlayspace`.

`fort_playspace<native><public> := interface<epic_internal>:`

### GetPlayers

* Get an `[]player`s in the current `fort_playspace`.

`GetPlayers<public>()<transacts>:[]player`

### GetTeamCollection

* Get the `fort_team_collection` for the current `fort_playspace`.

`GetTeamCollection<public>()<transacts>:fort_team_collection`

### PlayerAddedEvent

* Signaled when a `player` joins the `fort_playspace`. Returns a subscribable with a payload of the`fort_character` that entered the `fort_playspace`.

`PlayerAddedEvent<public>():listenable(player)`

### PlayerRemovedEvent

* Signaled when a `player` leaves the `fort_playspace`. Returns a subscribable with a payload of the`fort_character` that left the `fort_playspace`.

`PlayerRemovedEvent<public>():listenable(player)`

## Game

* Module import path: /Fortnite.com/Game

`Game<public> := module:`

### elimination\_result

* Result data for `fort_character` elimination events.

`elimination_result<native><public> := struct<epic_internal>:`

### EliminatedCharacter

* The `fort_character` eliminated from the match by `EliminatingCharacter`.

`EliminatedCharacter<native><public>:fort_character`

### EliminatingCharacter

* `fort_character` that eliminated `EliminatedCharacter` from the match. `EliminatingCharacter` will be false when `EliminatedCharacter` was eliminated through non-character actions, such as environmental damage.

`EliminatingCharacter<native><public>:?fort_character`

### positional

* Implemented by objects to allow reading position information.

`positional<native><public> := interface<epic_internal>:`

### GetTransform

* Returns the transform of the object.

`GetTransform<public>()<transacts>:transform`

### healthful

* Implemented by Fortnite objects that have health state and can be eliminated.

`healthful<native><public> := interface<epic_internal>:`

### GetHealth

* Returns the health state of the object. This value will between 0.0 and `GetMaxHealth`

`GetHealth<public>()<transacts>:float`

### SetHealth

* Sets the health state of the object to `Health`.
* Health state will be clamped between 1.0 and `GetMaxHealth`.
* Health state cannot be directly set to 0.0. To eliminate `healthful` objects use the `damageable.Damage` functions instead.

`SetHealth<public>(Health:float)<transacts>:void`

* Returns the maximum health of the object. This value will be between 1.0 and Inf. `GetMaxHealth<public>()<transacts>:float`
* Sets the maximum health state of the object.
* MaxHealth will be clamped between 1.0 and Inf.
* Current health state will be scaled up or down based on the scale difference between the old and new MaxHealth state. `SetMaxHealth<public>(MaxHealth:float)<transacts>:void`
* Implemented by Fortnite objects that have shields. A shield is a method of protection that can take incoming damage while leaving the health state unchanged.

### shieldable

`shieldable<native><public> := interface<epic_internal>:`

### GetShield

* Returns the shield state of the object. This value will between 0.0 and `MaxShield` `GetShield<public>()<transacts>:float`

### SetShield

* Sets the shield state of the object.
* Shield state will be clamped between 0.0 and `MaxShield`. `SetShield<public>(Shield:float)<transacts>:void`

### GetMaxShield

* Returns the maximum shield state of the object. This value will be between 0.0 and Inf.

`GetMaxShield<public>()<transacts>:float`

### SetMaxShield

* Sets the maximum shield state of the object.
* MaxShield will be clamped between 0.0 and Inf.
* Current shield state will be scaled up or down based on the scale difference between the old and new MaxShield state.

`SetMaxShield<public>(MaxShield:float)<transacts>:void`

### DamagedShieldEvent

* Signaled when the shield is damaged.

`DamagedShieldEvent<public>():listenable(damage_result)`

### HealedShieldEvent

* Signaled when the shield is healed.

`HealedShieldEvent<public>():listenable(healing_result)`

### damageable

* Implemented by Fortnite objects that can be damaged.

`damageable<native><public> := interface<epic_internal>:`

* Damage the `damageable` object anonymously by `Amount`. Setting `Amount` to less than 0 will cause no damage.
* Use `Damage(:damage_args):void` when damage is being applied from a known instigator and source. `Damage<public>(Amount:float):void`
* Damage the `damageable` object by `Args.Amount`. Setting `Amount` to less than 0 will cause no damage.

`Damage<public>(Args:damage_args):void`

### DamagedEvent

* Signaled when damage is applied to the `damageable` object.

`DamagedEvent<public>():listenable(damage_result)`

* Implemented by Fortnite objects that can be healed.

`healable<native><public> := interface<epic_internal>:`

* Heal the `healable` object anonymously by `Amount`. Setting `Amount` to less than 0 will cause no healing.
* Use `Heal(:healing_args):void` when healing is being applied from a known instigator and source.

`Heal<public>(Amount:float):void`

* Cause `Args.Amount` damage to the `damageable` object. Setting `Amount` to less than 0 will cause no damage.

`Heal<public>(Args:healing_args):void`

* Signaled when healing is applied to the `healable` object.

`HealedEvent<public>():listenable(healing_result)`

### damage\_args

* Parameters for common damage functions on Fortnite objects.

`damage_args<native><public> := struct:`

* Player, agent, etc. that instigated the damage to the object.

`Instigator<native><public>:?game_action_instigator = external {}`

* Player, weapon, vehicle, etc. that damaged the object.

`Source<native><public>:?game_action_causer = external {}`

* Amount of damage to apply to the object.

`Amount<native><public>:float`

* Results for damage events on Fortnite objects.

`damage_result<native><public> := struct<epic_internal>:`

* Object that was damaged.

`Target<native><public>:damageable`

* Amount of damage applied to `Target`.

`Amount<native><public>:float`

* Player, agent, etc. that instigated the damage to `Target`. Can be false when damage is instigated by code, the environment, etc.

`Instigator<native><public>:?game_action_instigator = external {}`

* Player, weapon, vehicle, etc. that damaged `Target`. Can be false when damage is caused by code, the environment, etc.

`Source<native><public>:?game_action_causer = external {}`

* Parameters for common healing functions on Fortnite objects.

`healing_args<native><public> := struct:`

* Player, agents, etc. that instigated the healing of the object.

`Instigator<native><public>:?game_action_instigator = external {}`

* Player, weapon, vehicle, etc. that healed the object.

`Source<native><public>:?game_action_causer = external {}`

* Amount of healing to apply to the object.

`Amount<native><public>:float`

* Results for healing events on Fortnite objects.

`healing_result<native><public> := struct<epic_internal>:`

* Object that was healed.

`Target<native><public>:healable`

* Amount of healing applied to `Target`.

`Amount<native><public>:float`

* Player, agent, etc. that instigated healing of the `Target`. Can be false when damage is instigated by code, the environment, etc.

`Instigator<native><public>:?game_action_instigator = external {}`

* Player, weapon, vehicle, etc. that healed `Target`. Can be false when damage is caused by code, the environment, etc.

`Source<native><public>:?game_action_causer = external {}`

* Implemented by Fortnite objects that initiate game actions, such as damage and heal. For example, player or agents.
* Event listeners often use `game_action_instigators` to calculate player damage scores.

`game_action_instigator<native><public> := interface<epic_internal>:`

* Implemented by Fortnite objects that can be passed through game action events, such as damage and heal.
* For example: player, vehicle, or weapon.
* Event Listeners often use `game_action_causer` to pass along additional information about what weapon caused the damage.
* Systems will then use that information for completing quests or processing game specific event logic.

`game_action_causer<native><public> := interface:`

## FortPlayerUtilities

`FortPlayerUtilities<public> := module:`

* Module import path: /Fortnite.com/FortPlayerUtilities
* Sends `InPlayer` back to the main game lobby. `(InPlayer:player).SendToLobby<native><public>()<transacts>:void`
* Succeeds if `InPlayer` is spectating the experience. Fails otherwise. `(InPlayer:player).IsSpectator<native><public>()<transacts><decides>:void`
* Returns an `[]player`s currently spectating `InPlayer`. `(InPlayer:player).GetPlayersSpectating<native><public>()<transacts>:[]player`
* Respawns the character for `InAgent` at the provided `RespawnPosition` and applies the yaw of `RespawnRotation`. `(InAgent:agent).Respawn<native><public>(RespawnPosition:vector3, RespawnRotation:rotation)<transacts>:void`

## Characters

`Characters<public> := module:`

* Module import path: /Fortnite.com/Characters
* Main API implemented by Fortnite characters.

`fort_character<native><public> := interface<unique><epic_internal>(positional, healable, healthful, damageable, shieldable, game_action_instigator, game_action_causer):`

### GetAgent

* Returns the agent associated with this `fort_character`. Use this when interacting with APIs that require an `agent` reference. `GetAgent<public>()<transacts><decides>:agent`

### EliminatedEvent

* Signaled when this `fort_character` is eliminated from the match. `EliminatedEvent<public>():listenable(elimination_result)`

### GetViewRotation

* Returns the rotation where this `fort_character` is looking or aiming at. `GetViewRotation<public>()<transacts>:rotation`

### GetViewLocation

* Returns the location where this `fort_character` is looking or aiming from. `GetViewLocation<public>()<transacts>:vector3`

### JumpedEvent

* Signaled when this `fort_character` jumps. Returns a listenable with a payload of this `fort_character`. `JumpedEvent<public>():listenable(fort_character)`

### CrouchedEvent

* Signaled when this `fort_character` changes crouch state.
* Sends `tuple` payload:
*
  * 0: the `fort_character` that changed crouch states.
*
  * 1: `true` if the character is crouching. `false` if the character is not crouching.

`CrouchedEvent<public>():listenable(tuple(fort_character, logic))`

### SprintedEvent

* Signaled when this `fort_character` changes sprint state.
* Sends `tuple` payload:
*
  * 0: the `fort_character` that changed sprint state.
*
  * 1: `true` if the character is sprinting. `false` if the character stopped sprinting. `<public>():listenable(tuple(fort_character, logic))`

### IsActive

* Succeeds if this `fort_character` is in the world and has not been eliminated. Most fort\_character actions will silently fail if this fails. Please test IsActive if you want to handle these failure cases rather than allow them to silently fail.

`IsActive<public>()<transacts><decides>:void`

### IsDBNO

* Succeeds if this `fort_character` is in the 'Down But Not Out' state. In this state the character is down but can still be revived by teammates for a period of time. `IsDownButNotOut<public>()<transacts><decides>:void`

### IsCrouching

* Succeeds if this `fort_character` is crouching. `IsCrouching<public>()<transacts><decides>:void`

### IsOnGround

* Succeeds if this `fort_character` is standing on the ground. `IsOnGround<public>()<transacts><decides>:void`

### IsInAir

* Succeeds if this `fort_character` is standing in the air. `IsInAir<public>()<transacts><decides>:void`

### IsInWater

* Succeeds if this `fort_character` is inside water volume. `IsInWater<public>()<transacts><decides>:void`

### IsFalling

* Succeeds if this `fort_character` is in falling locomotion state. `IsFalling<public>()<transacts><decides>:void`

### IsGliding

* Succeeds if this `fort_character` is in gliding locomotion state. `IsGliding<public>()<transacts><decides>:void`

### IsFlying

* Succeeds if this `fort_character` is in flying locomotion state. `IsFlying<public>()<transacts><decides>:void`

### Stasis

*   Parameters for `fort_character.PutInStasis` function:

    ```
       stasis_args<native><public> := struct:
       # Controls if `fort_character` can still turn while in stasis.
       AllowTurning<native><public>:logic = external {}

       # Controls if `fort_character` can still fall while in stasis.
       AllowFalling<native><public>:logic = external {}

       # Controls if `fort_character` can still perform emotes while in stasis.
       AllowEmotes<native><public>:logic = external {}
    ```
* Puts this `fort_character` into stasis, preventing certain types of movement specified by `Args`. `PutInStasis<public>(Args:stasis_args)<transacts>:void`
* Release this `fort_character` from stasis. `ReleaseFromStasis<public>()<transacts>:void`

### Show

* Sets this `fort_character` visibility to visible. `Show<public>():void`

### Hide

* Sets this `fort_character` visibility to invisible. `Hide<public>():void`

### SetVulnerability

* Control if this `fort_character` can be damaged. `SetVulnerability<public>(Vulnerable:logic)<transacts>:void`

### IsVulnerable

* Succeeds if this `fort_character` can be damaged. Fails if this `fort_character` cannot be damaged. `IsVulnerable<public>()<transacts><decides>:void`

### TeleportTo

* Teleports this `fort_character` to the provided `Position` and applies the yaw of `Rotation`. Will fail if the `Position` specified is e.g. outside of the playspace or specifies a place where the character cannot fit.

`TeleportTo<public>(Position:vector3, Rotation:rotation)<transacts><decides>:void`

* Returns the `fort_character` for `InAgent`. Fails if `InAgent` is not a `fort_character`. `(InAgent:agent).GetFortCharacter<native><public>()<transacts><decides>:fort_character`
* Returns a `game_action_instigator` interface for `InAgent`. `(InAgent:agent).GetInstigator<native><public>()<transacts>:game_action_instigator`
* Returns the `agent` for `InInstigator`. Fails if `InInstigator` is not an `agent`. `(InInstigator:game_action_instigator).GetInstigatorAgent<native><public>()<transacts><decides>:agent`

## Building

* Module import path: /Fortnite.com/Building

`Building<public> := module:`

## Assets

* Module import path: /Fortnite.com/Assets

'Assets := module:'

## Animation

* Module import path: /Fortnite.com/Animation
* Module import path: /Fortnite.com/Animation/PlayAnimation

`Animation<public> := module:`

`PlayAnimation<public> := module:`

`play_animation_result<native><public> := enum:`

* The animation completed successfully. `Completed`
* The animation was interrupted whilst playing. `Interrupted`
* The animation encountered an error during initialization or whilst playing. `Error`
* An interface for playing an animation on an object. `play_animation_controller<native><public> := interface<epic_internal>:`
* Play an animation sequence. `PlayAndAwait<public>(AnimationSequence:animation_sequence, ?PlayRate:float = external {}, ?StartPositionSeconds:float = external {}, ?BlendInTime:float = external {}, ?BlendOutTime:float = external {})<suspends>:play_animation_result`
* Start an animation sequence and obtain an instance to query and manipulate. `Play<public>(AnimationSequence:animation_sequence, ?PlayRate:float = external {}, ?StartPositionSeconds:float = external {}, ?BlendInTime:float = external {}, ?BlendOutTime:float = external {}):play_animation_instance`
* An animation instance created from play\_animation\_controller.Play that can be queried and manipulated. `play_animation_instance<native><public> := class<epic_internal>:`
* Returns the state of the animation playback. `GetState<native><public>()<transacts>:play_animation_state`
* Stops the animation. `Stop<native><public>():void`
* Event triggered when the animation is completed. `CompletedEvent<native><public>:listenable(tuple()) = external {}`
* Event triggered when the animation is interrupted. `InterruptedEvent<native><public>:listenable(tuple()) = external {}`
* Event triggered when the animation has finished to blend out. `BlendedInEvent<native><public>:listenable(tuple()) = external {}`
* Event triggered when the animation is beginning to blend out. `BlendingOutEvent<native><public>:listenable(tuple()) = external {}`
* Helper function that waits for the animation to complete or be interrupted. `Await<public>()<suspends>:play_animation_result = external {}`
* Helper function that succeeds if the state is Playing, BlendingIn, or BlendingOut. `IsPlaying<public>()<transacts><decides>:void = external {}`
* The potential states of a play animation instance. `play_animation_state<native><public> := enum:`
* The animation is blending in.

`BlendingIn`

* The animation has blended in, is playing, and has not begun blending out.

`Playing`

* The animation is playing and is blending out.

`BlendingOut`

* The animation completed successfully.

`Completed`

* The animation was stopped internally.

`Stopped`

* The animation was interrupted externally.

`Interrupted`

* An error occurred at creation or during playback.

`Error`

* Get the play\_animation\_controller for the specified character. `(InCharacter:fort_character).GetPlayAnimationController<native><public>()<transacts><decides>:play_animation_controller`

## AI

* Module import path: /Fortnite.com/AI

`AI<public> := module:`

`focus_interface<native><public> := interface<epic_internal>:`

* Look At specified location. Will never complete unless interrupted. `MaintainFocus<public>(Location:vector3)<suspends>:void`
* Look At specified Agent. Will never complete unless interrupted. `MaintainFocus<public>(Agent:agent)<suspends>:void`
* Get the focus\_interface interface for the specified character. `(InCharacter:fort_character).GetFocusInterface<native><public>()<transacts><decides>:focus_interface fort_leashable<native><public> := interface<epic_internal>:`
* Set custom leash position.
* 'InnerRadius' ranges from 0.0 to 20000.0 (in centimeters).
* 'OuterRadius' ranges from 0.0 to 20000.0 (in centimeters) and no less than 'InnerRadius'. `SetLeashPosition<public>(Location:vector3, InnerRadius:float, OuterRadius:float):void`
* Set the agent to be the new center of the leash.
* 'InnerRadius' ranges from 0.0 to 20000.0 (in centimeters).
* 'OuterRadius' ranges from 0.0 to 20000.0 (in centimeters) and no less than 'InnerRadius'. `SetLeashAgent<public>(Agent:agent, InnerRadius:float, OuterRadius:float):void`
* Removes the current leash. `ClearLeash<public>():void`
* Get the current fort\_leashable interface for the specified character. `(InCharacter:fort_character).GetFortLeashable<native><public>()<transacts><decides>:fort_leashable`

`navigation_target<native><public> := class<epic_internal>:`

*   Generate a navigation\_target from any position `MakeNavigationTarget<constructor><native><public>(Position:vector3):navigation_target`

    ## Generate a navigation\_target from an agent

    MakeNavigationTarget

    ## Result of a navigation request

    navigation\_result := enum: # The destination has been reached Reached # The destination has been partially reached (AllowPartialPath was used) PartiallyReached # Navigation has been interrupted before completion Interrupted # The navigating agent is blocked Blocked # The destination cannot be reached Unreachable

    movement\_type := class\<epic\_internal>:

    ## Module import path: /Fortnite.com/AI/movement\_types

    movement\_types := module: Walking:movement\_type = external {}

    ```
       Running<public>:movement_type = external {}
    ```

    navigatable := interface\<epic\_internal>: # Return the current destination of the character GetCurrentDestination():vector3

    ```
       # Navigate toward the specified target
       NavigateTo<public>(Target:navigation_target, ?MovementType:movement_type = external {}, ?ReachRadius:float = external {}, ?AllowPartialPath:logic = external {})<suspends>:navigation_result

       # Stop navigation
       StopNavigation<public>():void

       # Wait for a specific duration
       Wait<public>(?Duration:float = external {})<suspends>:void

       # Apply a multiplier on the movement speed (Multiplier is clamped between 0.5 and 2)
       SetMovementSpeedMultiplier<public>(Multiplier:float):void
    ```

    ## Get the navigatable interface for the specified character

    (InCharacter:fort\_character).GetNavigatable():navigatable

    ## Inherit from this to create a custom NPC behavior.

    ## The npc\_behavior can be defined for a character in a CharacterDefinition asset, or in a npc\_spawner\_device.

    npc\_behavior := class: # This function is called when the NPC is added to the simulation. OnBegin\<native\_callable>():void = external {}

    ```
       # This function is called when the NPC is removed from the simulation.
       OnEnd<native_callable><public>():void = external {}

       # Returns the agent associated with this behavior.
       GetAgent<native><public>()<transacts><decides>:agent
    ```

    ## Returns the `npc_behavior` for `InAgent`.

    (InAgent:agent).GetNPCBehavior():npc\_behavior
