# 📗 Unreal Engine Digest

## UI

`ui<public> := module:`

### GetPlayerUI

* Returns the `player_ui` vk\_component associated with `Player`.
* Fails if there is no `player_ui` associated with `Player`. `GetPlayerUI<native><public>(Player:player)<transacts><decides>:player_ui`

### player\_ui

* The main interface for adding and removing `widget`s to a player's UI. `player_ui<native><public> := class<final><epic_internal>:`

### widget

`widget<native><public> := class<abstract><unique><epic_internal>:`

* Base class for all UI elements drawn on the `player`'s screen.
* Shows or hides the `widget` without removing itself from the containing `player_ui`. `SetVisibility<native><public>(InVisibility:widget_visibility):void`
* Returns the current `widget_visibility` state. `GetVisibility<native><public>():widget_visibility`
* Enables or disables whether the `player` can interact with this `widget`. `SetEnabled<native><public>(InIsEnabled:logic):void`
* `true` if this `widget` can be modified interactively by the player. `IsEnabled<native><public>():logic`
* Returns the `widget`'s parent `widget`.
* Fails if no parent exists, such as if this `widget` is not in the `player_ui` or is itself the root `widget`. `GetParentWidget<native><public>()<transacts><decides>:widget`
* Returns the `widget` that added this `widget` to the `player_ui`. The root `widget` will return itself.
* Fails if this `widget` is not in the `player_ui`. `GetRootWidget<native><public>()<transacts><decides>:widget`

#### AddWidget

* Adds `Widget` to this `player_ui` using default `player_ui_slot` configuration options. `AddWidget<native><public>(Widget:widget):void`
* Adds `Widget` to this `player_ui` using `Slot` for configuration options. `AddWidget<native><public>(Widget:widget, Slot:player_ui_slot):void`
* Removes `Widget` from this `player_ui`. `RemoveWidget<native><public>(Widget:widget):void`

#### widget configuration options.

`player_ui_slot<native><public> := struct:`

* Controls `widget` rendering order. Greater values will be draw in front of lesser values.

`ZOrder<native><public>:type {_X:int where 0 <= _X, _X <= 2147483647} = external {}`

* Controls `widget` input event consumption.

`InputMode<native><public>:ui_input_mode = external {}`

* `widget` input consumption mode.

`ui_input_mode<native><public> := enum:`

* `widget` does not consume any input.

`None`

* `widget` consumes all inputs

`All`

* Parameters for `event`s signalled by a `widget`.

`widget_message<native><public> := struct:`

* The `player` that triggered the `event`.

`Player<native><public>:player`

* The `widget` that triggered the `event`.

`Source<native><public>:widget`

* Used by `widget.SetVisibility` determine how a `widget` is shown in the user interface.

`widget_visibility<native><public> := enum:`

* The `widget` is visible and occupies layout space.

`Visible`

* The `widget` is invisible and does not occupy layout space.

`Collapsed`

* The `widget` is invisible and occupies layout space.

`Hidden`

* Used by`widget` orientation modes.

`alignment<native><public> := enum:`

* Orient `widget`s from left to right.

`Horizontal`

* Orient `widget`s from top to bottom.

`Vertical`

* `widget` horizontal alignment mode.

`horizontal_alignment<native><public> := enum:`

* Center `widget` horizontally within the slot.

`Center`

* Align `widget` to the left of the slot.

`Left`

* Align `widget` to the right of the slot.

`Right`

* `widget` fills the slot horizontally.

`Fill`

* `widget` vertical alignment mode.

`vertical_alignment<native><public> := enum:`

* Center `widget` vertically within the slot.

`Center`

* Align `widget` to the top of the slot.

`Top`

* Align `widget` to the bottom of the slot.

`Bottom`

* `widget` fills the slot vertically.

`Fill`

* The anchors of a `widget` determine its the position and sizing relative to its parent.
* `anchor`s range from `(0.0, 0.0)` (left, top) to `(1.0, 1.0)` (right, bottom).

`anchors<native><public> := struct:`

* Holds the minimum anchors, (left, top). The valid range is between `0.0` and `1.0`.

`Minimum<native><public>:vector2 = external {}`

* Holds the maximum anchors, (right, bottom). The valid range is between `0.0` and `1.0`.

`Maximum<native><public>:vector2 = external {}`

* Specifies the gap outside each edge separating a `widget` from its neighbors.
* Distance is measured in units where `1.0` unit is the width of a pixel at 1080p resolution.

`margin<native><public> := struct:`

* The left edge spacing.

`Left<native><public>:float = external {}`

* The top edge spacing.

`Top<native><public>:float = external {}`

* The right edge spacing.

`Right<native><public>:float = external {}`

* The bottom edge spacing.

`Bottom<native><public>:float = external {}`

### button

`button<native><public> := class<final>(widget):`

* Button is a container of a single child widget slot and fires the OnClick event when the button is clicked.
* The child widget of the button. Used only during initialization of the widget and not modified by SetSlot.

`Slot<native><public>:button_slot`

* Sets the child widget slot.

`SetWidget<native><public>(InSlot:button_slot):void`

* Subscribable event that fires when the button is clicked.

`OnClick<public>():listenable(widget_message) = external {}`

* Slot for button widget.

`button_slot<native><public> := struct:`

* The widget assigned to this slot.

`Widget<native><public>:widget`

\*Horizontal alignment of the widget inside the slot.

`HorizontalAlignment<native><public>:horizontal_alignment = external {}`

* Vertical alignment of the widget inside the slot.

`VerticalAlignment<native><public>:vertical_alignment = external {}`

* Empty distance in pixels that surrounds the widget inside the slot. Assumes 1080p resolution.

`Padding<native><public>:margin = external {}`

### canvas

`canvas<native><public> := class<final>(widget):`

* Canvas is a container widget that allows for arbitrary positioning of widgets in the canvas' slots.
* The child widgets of the canvas. Used only during initialization of the widget and not modified by Add/RemoveWidget.

`Slots<native><public>:[]canvas_slot = external {}`

* Adds a new child slot to the canvas.

`AddWidget<native><public>(Slot:canvas_slot):void`

* Removes a slot containing the given widget.

`RemoveWidget<native><public>(Widget:widget):void`

* Slot for a canvas widget.

`canvas_slot<native><public> := struct:`

* The border for the margin and how the widget is resized with its parent.
* Values are defined between 0.0 and 1.0.

`Anchors<native><public>:anchors = external {}`

* The offset that defined the size and position of the widget.
* When the anchors are well defined, the Offsets.Left represent the distance in pixels from the Anchors Minimum.X, the Offsets.Bottom represent the distance in pixel from the Anchors Maximum.Y, effectively controlling the desired widget size. When the anchors are not well defined, the Offsets.Left and Offsets.Top represent the widget position and Offsets.Right and Offset.Bottom represent the widget size.

`Offsets<native><public>:margin = external {}`

* When true we use the widget's desired size. The size calculated by the Offsets is ignored.

`SizeToContent<native><public>:logic = external {}`

* Alignment is the pivot/origin point of the widget.
* Starting in the upper left at (0.0,0.0), ending in the lower right at (1.0,1.0).

`Alignment<native><public>:vector2 = external {}`

* Z Order of this slot relative to other slots in this canvas panel.
* Higher values are rendered last (and so they will appear to be on top)

`ZOrder<native><public>:type {_X:int where 0 <= _X, _X <= 2147483647} = external {}`

* The widget assigned to this slot.

`Widget<native><public>:widget`

* Make a canvas slot for fixed position widget.
* If Size is set, then the Offsets is calculated and the SizeToContent is set to false.
* If Size is not set, then Right and Bottom are set to zero and are not used. The widget size will be automatically calculated. The SizeToContent is set to true.
* The widget is not anchored and will not move if the parent is resized.
* The Anchors is set to zero.

`MakeCanvasSlot<native><public>(Widget:widget, Position:vector2, ?Size:vector2 = external {}, ?ZOrder:type {_X:int where 0 <= _X, _X <= 2147483647} = external {}, ?Alignment:vector2 = external {})<computes>:canvas_slot`b

### color\_block

`color_block<native><public> := class<final>(widget):`

* A solid color widget.
* The color of the widget. Used only during initialization of the widget and not modified by SetColor.

`DefaultColor<native><public>:color = external {}`

* The opacity of the widget. Used only during initialization of the widget and not modified by SetOpacity.

`DefaultOpacity<native><public>:type {_X:float where 0.000000 <= _X, _X <= 1.000000} = external {}`

* The size this widget desired to be displayed in. Used only during initialization of the widget and not modified by SetDesiredSize.

`DefaultDesiredSize<native><public>:vector2 = external {}`

* Sets the widget's color.

`SetColor<native><public>(InColor:color):void`

* Gets the widget's color.

`GetColor<native><public>():color`

* Sets the widgets's opacity.

`SetOpacity<native><public>(InOpacity:type {_X:float where 0.000000 <= _X, _X <= 1.000000}):void`

* Gets the widget's opacity.

`GetOpacity<native><public>():type {_X:float where 0.000000 <= _X, _X <= 1.000000}`

* Sets the size this widget desired to be displayed in.

`SetDesiredSize<native><public>(InDesiredSize:vector2):void`

* Gets the size this widget desired to be displayed in.

`GetDesiredSize<native><public>():vector2`

### image\_tiling

`image_tiling<native><public> := enum:`

* Tiling options values
* Stretch the image to fit the available space.

`Stretch`

* Repeat/Wrap the image to fill the available space.

`Repeat`

### texture\_block

`texture_block<native><public> := class(widget):`

* A widget to display a texture.
* The image to render. Used only during initialization of the widget and not modified by SetImage.

`DefaultImage<native><public>:texture`

* Tinting applied to the image. Used only during initialization of the widget and not modified by SetTint.

`DefaultTint<native><public>:color = external {}`

* The size this widget desired to be displayed in. Used only during initialization of the widget and not modified by SetDesiredSize.

`DefaultDesiredSize<native><public>:vector2 = external {}`

* The horizontal tiling option. Used only during initialization of the widget and not modified by SetTiling.

`DefaultHorizontalTiling<native><public>:image_tiling = external {}`

* The vertical tiling option. Used only during initialization of the widget and not modified by SetTiling.

`DefaultVerticalTiling<native><public>:image_tiling = external {}`

* Sets the image to render.

`SetImage<native><public>(InImage:texture):void`

* Gets the image to render.

`GetImage<native><public>():texture`

* Sets the tint applied to the image. `SetTint<native><public>(InColor:color):void`
* Gets the tint applied to the image.

`GetTint<native><public>():color`

* Sets the size this widget desired to be displayed in.

`SetDesiredSize<native><public>(InDesiredSize:vector2):void`

* Gets the size this widget desired to be displayed in.

`GetDesiredSize<native><public>():vector2`

* Sets the tiling option when the image is smaller than the allocated size.

`SetTiling<native><public>(InHorizontalTiling:image_tiling, InVerticalTiling:image_tiling):void`

* Gets the tiling option.

`GetTiling<native><public>():tuple(image_tiling, image_tiling)`

### overlay

`overlay<native><public> := class<final>(widget):`

* Overlay is a container consisting of widgets stacked on top of each other.
* The child widgets of the overlay. Used only during initialization of the widget and not modified by Add/RemoveWidget.

`Slots<native><public>:[]overlay_slot = external {}`

* Add a new child slot to the overlay. Slots are added at the end.

`AddWidget<native><public>(Slot:overlay_slot):void`

* Removes a slot containing the given widget

`RemoveWidget<native><public>(Widget:widget):void`

* Slot for an overlay widget

`overlay_slot<native><public> := struct:`

* The widget assigned to this slot.

`Widget<native><public>:widget`

* Horizontal alignment of the widget inside the slot.
* This alignment is only applied after the layout space for the widget slot is created and determines the widget alignment within that space.

`HorizontalAlignment<native><public>:horizontal_alignment = external {}`

* Vertical alignment of the widget inside the slot.
* This alignment is only applied after the layout space for the widget slot is created and determines the widget alignment within that space.

`VerticalAlignment<native><public>:vertical_alignment = external {}`

* Empty distance in pixels that surrounds the widget inside the slot. Assumes 1080p resolution.

`Padding<native><public>:margin = external {}`

### stack\_box

* Stack box is a container of a list of widgets stacked either vertically or horizontally.

`stack_box<native><public> := class<final>(widget):`

* The child widgets of the stack box. Used only during initialization of the widget and not modified by Add/RemoveWidget.

`Slots<native><public>:[]stack_box_slot = external {}`

* The orientation of the stack box. Either stack widgets horizontal or vertical.

`Orientation<native><public>:orientation`

* Add a new child slot to the stack box. Slots are added at the end.

`AddWidget<native><public>(Slot:stack_box_slot):void`

* Removes a slot containing the given widget

`RemoveWidget<native><public>(Widget:widget):void`

* Slot for a stack\_box widget

`stack_box_slot<native><public> := struct:`

* The widget assigned to this slot.

`Widget<native><public>:widget`

* Horizontal alignment of the widget inside the slot.
* This alignment is only applied after the layout space for the widget slot is created and determines the widget alignment within that space.

`HorizontalAlignment<native><public>:horizontal_alignment = external {}`

* Vertical alignment of the widget inside the slot.
* This alignment is only applied after the layout space for the widget slot is created and determines the widget alignment within that space.

`VerticalAlignment<native><public>:vertical_alignment = external {}`

* Empty distance in pixels that surrounds the widget inside the slot. Assumes 1080p resolution.

`Padding<native><public>:margin = external {}`

* The available space will be distributed proportionally.
* If not set, the slot will use the desired size of the widget.

`Distribution<native><public>:?float = external {}`

### text\_justification

`text_justification<native><public> := enum:`

* Text justification
* The Left and Right value will flip when the local culture is right-to-left.

`Left`

`Center`

`Right`

`InvariantLeft`

`InvariantRight`

### text\_overflow\_policy

`text_overflow_policy<native><public> := enum:`

* Text overflow policy values:

`Clip`

`Ellipsis`

### text\_base

`text_base<native><public> := class<abstract>(widget):`

* Base widget for text widget.

### DefaultText

`DefaultText<native><localizes><public>:message = external {}`

* The text to display to the user. Used only during initialization of the widget and not modified by SetText.
* The color of the displayed text. Used only during initialization of the widget and not modified by SetTextColor.

`DefaultTextColor<native><public>:color = external {}`

* The opacity of the displayed text. Used only during initialization of the widget and not modified by SetTextOpacity.

`DefaultTextOpacity<native><public>:type {_X:float where 0.000000 <= _X, _X <= 1.000000} = external {}`

* The justification to display to the user. Used only during initialization of the widget and not modified by SetJustification.

`DefaultJustification<native><public>:text_justification = external {}`

* The policy that determine what happens when the text is longer than its allowed length.
* Used only during initialization of the widget and not modified by SetOverflowPolicy.

`DefaultOverflowPolicy<native><public>:text_overflow_policy = external {}`

### SetText

`SetText<native><public>(InText:message):void`

* Sets the text displayed in the widget.
* Gets the text currently in the widget.

`GetText<native><public>():string`

* Sets the text justification in the widget.

`SetJustification<native><public>(InJustification:text_justification):void`

* Gets the text justification in the widget.

`GetJustification<native><public>():text_justification`

* Sets the policy that determine what happens when the text is longer than its allowed length.

`SetOverflowPolicy<native><public>(InOverflowPolicy:text_overflow_policy):void`

* Gets the policy that determine what happens when the text is longer than its allowed length.

`GetOverflowPolicy<native><public>():text_overflow_policy`

* Sets the color of the displayed text.

`SetTextColor<native><public>(InColor:color):void`

* Gets the color of the displayed text.

`GetTextColor<native><public>():color`

* Sets the opacity of the displayed text.

`SetTextOpacity<native><public>(InOpacity:type {_X:float where 0.000000 <= _X, _X <= 1.000000}):void`

* Gets the opacity of the displayed text.

`GetTextOpacity<native><public>():type {_X:float where 0.000000 <= _X, _X <= 1.000000}`

## Diagnostics

`Diagnostics<public> := module:`

`Module import path: /UnrealEngine.com/Temporary/Diagnostics`

### debug\_draw

`debug_draw<native><public> := class:`

* Enumerated presets for policies describing a desired draw duration.

`debug_draw_duration_policy<native><public> := enum:`

`SingleFrame`

`FiniteDuration`

`Persistent`

### debug\_draw\_channel

`debug_draw_channel<native><public> := class<abstract>:`

* debug\_draw\_channel is the base class used to define debug draw channels.
* debug draw class to draw debug shapes on screen.
* Channel will be used to clear specific debug draw.

`Channel<native><public>:subtype(debug_draw_channel) = external {}`

* Show Debug Draw for the channel for all users.

`ShowChannel<native><public>()<transacts>:void`

* Hide Debug Draw for the channel for all users.

`HideChannel<native><public>()<transacts>:void`

* Clears all debug draw for the channel.

`ClearChannel<native><public>()<transacts>:void`

* Clears all debug draw from this debug\_draw instance.

`Clear<native><public>()<transacts>:void`

### draw

`Draw<native><public>`

* Draws using provided parameters.
* Draws a sphere at the named location, and using the provided draw parameters.

`DrawSphere<native><public>(Center:vector3, ?Radius:float = external {}, ?Color:color = external {}, ?NumSegments:int = external {}, ?Thickness:float = external {}, ?DrawDurationPolicy:debug_draw_duration_policy = external {}, ?Duration:float = external {})<transacts>:void`

* Draws a box at the named location, and using the provided draw parameters

`DrawBox<native><public>(Center:vector3, Rotation:rotation, ?Extent:vector3 = external {}, ?Color:color = external {}, ?Thickness:float = external {}, ?DrawDurationPolicy:debug_draw_duration_policy = external {}, ?Duration:float = external {})<transacts>:void`

* Draws a capsule at the named location, and using the provided draw parameters.

`DrawCapsule<native><public>(Center:vector3, Rotation:rotation, ?Height:float = external {}, ?Radius:float = external {}, ?Color:color = external {}, ?Thickness:float = external {}, ?DrawDurationPolicy:debug_draw_duration_policy = external {}, ?Duration:float = external {})<transacts>:void`

* Draws a cone at the named location, and using the provided draw parameters.

`DrawCone<native><public>(Origin:vector3, Direction:vector3, ?Height:float = external {}, ?NumSides:int = external {}, ?AngleWidthRadians:float = external {}, ?AngleHeightRadians:float = external {}, ?Color:color = external {}, ?Thickness:float = external {}, ?DrawDurationPolicy:debug_draw_duration_policy = external {}, ?Duration:float = external {})<transacts>:void`

* Draws a cylinder at the named location, and using the provided draw parameters.

`DrawCylinder<native><public>(Start:vector3, End:vector3, ?NumSegments:int = external {}, ?Radius:float = external {}, ?Color:color = external {}, ?Thickness:float = external {}, ?DrawDurationPolicy:debug_draw_duration_policy = external {}, ?Duration:float = external {})<transacts>:void`

* Draws a line from Start to End locations, and using the provided draw parameters.

`DrawLine<native><public>(Start:vector3, End:vector3, ?Color:color = external {}, ?Thickness:float = external {}, ?DrawDurationPolicy:debug_draw_duration_policy = external {}, ?Duration:float = external {})<transacts>:void`

* Draws a point at the named location, and using the provided draw parameters.

`DrawPoint<native><public>(Position:vector3, ?Color:color = external {}, ?Thickness:float = external {}, ?DrawDurationPolicy:debug_draw_duration_policy = external {}, ?Duration:float = external {})<transacts>:void`

* Draws an arrow pointing from Start to End locations, and using the provided draw parameters.

`DrawArrow<native><public>(Start:vector3, End:vector3, ?ArrowSize:float = external {}, ?Color:color = external {}, ?Thickness:float = external {}, ?DrawDurationPolicy:debug_draw_duration_policy = external {}, ?Duration:float = external {})<transacts>:void`

### log\_level

`log_level<native><public> := enum:`

*   log levels available for various log commands

    `Debug`

    `Verbose`

    `Normal`

    `Warning`

    `Error`

### log\_channel

`log_channel<native><public> := class<abstract>:`

* log\_channel is the base class used to define log channels. When printing a message to a log, the log channel class name will be prefixed to the output message.

### log

`log<native><public> := class:`

* log class to send messages to the default log
* Channel class name will be added as a prefix used when printing the message e.g. '\[log\_channel]: #Message

`Channel<native><public>:subtype(log_channel)`

* Sets the default log level of the displayed message. See log\_level enum for more info on log levels. Defaults to log\_level.Normal.

`DefaultLevel<native><public>:log_level = external {}`

* Print message using the given log level

`(log:)Print<native><public>(Message:string, ?Level:log_level = external {})<computes>:void`

* Prints current script call stack using the give log level

`PrintCallStack<native><public>(?Level:log_level = external {})<computes>:void`

### Curves

`Curves<public> := module:`

`Module import path: /UnrealEngine.com/Temporary/Curves`

`editable_curve<native><public> := class<final><concrete>:`

* Evaluates this float curve at the specified time and returns the result as a float

`Evaluate<native><public>(Time:float):float`

## SpatialMath

`using {/Verse.org/Native}`

* Module import path: `/UnrealEngine.com/Temporary/SpatialMath`

`SpatialMath<public> := module:`

`@editable`

`@import_as("/Script/EpicGamesTemporary.FVerseRotation")`

`rotation<native><public> := struct<concrete>:`

* Makes a `rotation` from `Axis` and `AngleRadians` using a left-handed sign convention (e.g. a positive rotation around +Z takes +X to +Y). If `Axis.IsAlmostZero[]`, make the identity rotation.

`MakeRotation<native><public>(Axis:vector3, AngleRadians:float)<varies>:rotation`

* Makes a `rotation` by applying `YawRightDegrees`, `PitchUpDegrees`, and `RollClockwiseDegrees`, in that order: First a yaw about the Z axis with a positive angle indicating a clockwise rotation when viewed from above, then a pitch about the new Y axis with a positive angle indicating 'nose up' followed by a roll about the new X axis axis with a positive angle indicating a clockwise rotation when viewed along +X. Note that these conventions differ from `MakeRotation` but match `ApplyYaw`, `ApplyPitch`, and `ApplyRoll`.

`MakeRotationFromYawPitchRollDegrees<native><public>(YawRightDegrees:float, PitchUpDegrees:float, RollClockwiseDegrees:float)<varies>:rotation`

* Makes the identity `rotation`.

`IdentityRotation<native><public>()<converges>:rotation`

* Returns the 'distance' between `Rotation1` and `Rotation2`. The result will be between:
* `0.0`, representing equivalent rotations and
* `1.0` representing rotations which are 180 degrees apart (i.e., the shortest rotation between them is 180 degrees around some axis).

### distance

`Distance<native><public>(Rotation1:rotation, Rotation2:rotation)<varies>:float`

* Returns the 'smallest angular distance' between `Rotation1` and `Rotation2` in radians.

`AngularDistance<native><public>(Rotation1:rotation, Rotation2:rotation)<varies>:float`

### rotation

* Makes a `rotation` by applying `PitchUpRadians` of right-handed rotation around the local +Y axis to `InitialRotation`.

`(InitialRotation:rotation).ApplyPitch<native><public>(PitchUpRadians:float)<transacts>:rotation`

* Makes a `rotation` by applying `RollClockwiseRadians` of right-handed rotation around the local +X axis to `InitialRotation`.

`(InitialRotation:rotation).ApplyRoll<native><public>(RollClockwiseRadians:float)<transacts>:rotation`

* Makes a `rotation` by applying `YawRightRadians` of left-handed rotation around the local +Z axis to `InitialRotation`.

`(InitialRotation:rotation).ApplyYaw<native><public>(YawRightRadians:float)<transacts>:rotation`

* Makes a `rotation` by applying `AngleRadians` of left-handed rotation around the world +X axis to `InitialRotation`.

`(InitialRotation:rotation).ApplyWorldRotationX<native><public>(AngleRadians:float)<transacts>:rotation`

* Makes a `rotation` by applying `AngleRadians` of left-handed rotation around the world +Y axis to `InitialRotation`.

`(InitialRotation:rotation).ApplyWorldRotationY<native><public>(AngleRadians:float)<transacts>:rotation`

* Makes a `rotation` by applying `AngleRadians` of left-handed rotation around the world +Z axis to `InitialRotation`.

`(InitialRotation:rotation).ApplyWorldRotationZ<native><public>(AngleRadians:float)<transacts>:rotation`

* Makes a `rotation` by applying `AngleRadians` of left-handed rotation around the local +Y axis to `InitialRotation`.

`(InitialRotation:rotation).ApplyLocalRotationY<public>(AngleRadians:float)<transacts>:rotation = external {}`

* Makes a `rotation` by applying `AngleRadians` of left-handed rotation around the local +Z axis to `InitialRotation`.

`(InitialRotation:rotation).ApplyLocalRotationZ<public>(AngleRadians:float)<transacts>:rotation = external {}`

* Makes a `rotation` by composing `AdditionalRotation` to `InitialRotation`.

`(InitialRotation:rotation).RotateBy<native><public>(AdditionalRotation:rotation)<transacts>:rotation`

* Makes a `rotation` by composing the inverse of `RotationToRemove` from `InitialRotation`. such that InitialRotation = RotateBy(UnrotateBy(InitialRotation, RotationToRemove), RotationToRemove). This is equivalent to `RotateBy(InitialRotation, InvertRotation(RotationToRemove)) (InitialRotation:rotation).UnrotateBy<native><public>(RotationToRemove:rotation)<transacts>:rotation`
* Makes an `[]float` with three elements:
* yaw degrees of `rotation`
* pitch degrees of `rotation`
* roll degrees of `rotation`
* using the conventions of `MakeRotationFromYawPitchRollDegrees`.

`(Rotation:rotation).GetYawPitchRollDegrees<native><public>()<varies>:[]float`

* Makes a `vector3` from the axis of `rotation`.
* If `rotation` is nearly identity, this will return the +X axis. See also `GetAngle`. `(Rotation:rotation).GetAxis<native><public>()<varies>:vector3`
* Returns the radians of `rotation` around the axis of `rotation`. See also `GetAxis`. `(Rotation:rotation).GetAngle<native><public>()<varies>:float`
* Makes the smallest angular `rotation` from `InitialRotation` to `FinalRotation` such that:
* `InitialRotation.RotateBy(MakeShortestRotationBetween(InitialRotation, FinalRotation)) = FinalRotation` and
* `MakeShortestRotationBetween(InitialRotation, FinalRotation)?.GetAngle()` is as small as possible.

`MakeShortestRotationBetween<native><public>(InitialRotation:rotation, FinalRotation:rotation)<transacts>:rotation`

* Makes the smallest angular `rotation` from `InitialVector` to `FinalVector` such that:
* `InitialVector.RotateBy(MakeShortestRotationBetween(InitialVector, Vector)) = FinalVector` and
* `MakeShortestRotationBetween(InitialVector, FinalVector)?.GetAngle()` is as small as possible.

`MakeShortestRotationBetween<native><public>(InitialVector:vector3, FinalVector:vector3)<transacts>:rotation`

* Makes a new `rotation` from the component wise subtraction of the Euler angle components in `RotationA` by the Euler angle components in `RotationB` and ensures the returned value is normalized.

`MakeComponentWiseDeltaRotation<native><public>(RotationA:rotation, RotationB:rotation)<transacts>:rotation`

* Used to perform spherical linear interpolation between `From` (when `Parameter = 0.0`) and `To` (when `Parameter = 1.0`). Expects that `0.0 <= Parameter <= 1.0`.

`Slerp<native><public>(InitialRotation:rotation, FinalRotation:rotation, Parameter:float)<transacts><decides>:rotation`

* Makes a `vector3` by applying `Rotation` to `Vector`.

`(Rotation:rotation).RotateVector<native><public>(Vector:vector3)<transacts>:vector3`

* Makes a `vector3` by applying the inverse of `Rotation` to `Vector`.

`(Rotation:rotation).UnrotateVector<native><public>(Vector:vector3)<transacts>:vector3`

* Makes a `rotation` by inverting `Rotation` such that `ApplyRotation(Rotation, Rotation.Invert())) = IdentityRotation`.

`(Rotation:rotation).Invert<native><public>()<transacts>:rotation`

* Returns `Rotation` if it does not contain `NaN`, `Inf` or `-Inf`.

`(Rotation:rotation).IsFinite<native><public>()<computes><decides>:rotation`

* Makes a unit `vector3` pointing in the local space _forward_ direction in world space coordinates.
* This is equivalent to: `RotateVector(Rotation, vector3{X:=1.0, Y:=0.0, Z:=0.0})`.

`(Rotation:rotation).GetLocalForward<public>()<transacts>:vector3 = external {}`

* Makes a unit `vector3` pointing in the the local space _right_ direction in world space coordinates.
* This is equivalent to: `RotateVector(Rotation, vector3{X:=0.0, Y:=1.0, Z:=0.0})`.

\`(Rotation:rotation).GetLocalRight():vector3 = external {}

* Makes a unit `vector3` pointing in the local space _up_ direction in world space coordinates.
* This is equivalent to: `RotateVector(Rotation, vector3{X:=0.0, Y:=0.0, Z:=1.0})`. `(Rotation:rotation).GetLocalUp<public>()<transacts>:vector3 = external {}`
* Makes a `string` representation of `rotation` in axis/degrees format with a left-handed sign convention.
* `ToString(MakeRotation(vector3{X:=1.0, Y:=0.0, Z:=0.0}, PiFloat/2.0))` produces the string: `"Axis: {x=1.000000,y=0.000000,z=0.000000} Angle: 90.000000"`. `ToString<native><public>(Rotation:rotation)<varies>:string`
* Returns radians from `Degrees`. `DegreesToRadians<public>(Degrees:float)<varies>:float = external {}`
* Returns degrees from `Radians`. `RadiansToDegrees<public>(Radians:float)<varies>:float = external {}`

### transform

* A combination of scale, rotation, and translation, applied in that order. `transform<native><public> := struct<concrete><computes>:`
* @editable
* The scale of this `transform`.

`Scale<native><public>:vector3 = external {}`

* @editable
* The rotation of this `transform`.

`Rotation<native><public>:rotation = external {}`

* @editable
* The location of this `transform`.

`Translation<native><public>:vector3 = external {}`

### vector

* Makes a `vector3` by applying `InTransform` to `InVector`. `TransformVector<native><public>(InTransform:transform, InVector:vector3)<varies>:vector3`
* Makes a `vector3` by applying `InTransform` to `InVector` without applying `InTransform.Scale`. `TransformVectorNoScale<native><public>(InTransform:transform, InVector:vector3)<varies>:vector3`
* 2-dimensional vector with `float` components. `vector2<native><public> := struct<concrete><computes><persistable>:`
* @editable

`X<native><public>:float = external {}`

* @editable

`Y<native><public>:float = external {}`

* Makes a `vector2` by inverting the `SurfaceNormal` component of `Direction`.
* Fails if `not SurfaceNormal.MakeUnitVector[]`.

`ReflectVector<native><public>(Direction:vector2, SurfaceNormal:vector2)<varies><decides>:vector2`

* Returns the dot product of `V1` and `V2`. `DotProduct<native><public>(V1:vector2, V2:vector2)<varies>:float`
* Returns the Euclidean distance between `V1` and `V2`. `Distance<native><public>(V1:vector2, V2:vector2)<varies>:float`
* Returns the squared Euclidean distance between `V1` and `V2`. `DistanceSquared<native><public>(V1:vector2, V2:vector2)<varies>:float`
* Makes a unit length `vector3` pointing in the same direction of `V`.
* Fails if `V.IsAlmostZero[] or not V.IsFinite[]`. `(V:vector2).MakeUnitVector<native><public>()<varies><decides>:vector2`
* Returns the length of `V`. `(V:vector2).Length<public>()<varies>:float = external {}`
* Returns the squared length of `V`. `(V:vector2).LengthSquared<public>()<varies>:float = external {}`
* Used to linearly interpolate/extrapolate between `From` (when `Parameter = 0.0`) and `To` (when `Parameter = 1.0`). Expects that all arguments are finite.
* Returns `From*(1 - Parameter) + To*Parameter`. `Lerp<public>(From:vector2, To:vector2, Parameter:float)<varies>:vector2 = external {}`
* Makes a `string` representation of `V`. `ToString<native><public>(V:vector2)<varies>:string`
* Makes a `vector2` by inverting the signs of `Operand`. `prefix'-'<public>(Operand:vector2)<computes>:vector2 = external {}`
* Makes a `vector2` by component-wise addition of `Left` and `Right`. `operator'+'<public>(Left:vector2, Right:vector2)<computes>:vector2 = external {}`
* Makes a `vector2` by component-wise subtraction of `Right` from `Left`. `operator'-'<public>(Left:vector2, Right:vector2)<computes>:vector2 = external {}`
* Makes a `vector2` by component-wise multiplication of `Left` and `Right`. `operator'*'<public>(Left:vector2, Right:float)<computes>:vector2 = external {}`
* Makes a `vector2` by multiplying the components of `Right` by `Left`. `operator'*'<public>(Left:float, Right:vector2)<computes>:vector2 = external {}`
* Makes a `vector2` by dividing the components of `Left` by `Right`. `operator'/'<public>(Left:vector2, Right:float)<computes>:vector2 = external {}`
* Makes a `vector2` by component-wise division of `Left` by `Right`. `operator'/'<public>(Left:vector2, Right:vector2)<computes>:vector2 = external {}`
* Makes a `vector2` by converting the components of `V` to `float`s. `ToVector2<public>(V:vector2i)<transacts>:vector2 = external {}`
* Returns `V` if all components are finite.
* Fails if any of the components are not finite. `(V:vector2).IsFinite<public>()<computes><decides>:vector2 = external {}`
* Succeeds when each component of `V` is within `AbsoluteTolerance` of `0.0`. `(V:vector2).IsAlmostZero<public>(AbsoluteTolerance:float)<computes><decides>:void = external {}`
* Succeeds when each component of `V1` and `V2` are within `AbsoluteTolerance` of each other. `IsAlmostEqual<public>(V1:vector2, V2:vector2, AbsoluteTolerance:float)<computes><decides>:void = external {}`
* 2-dimensional vector with `int` components. `vector2i<native><public> := struct<concrete><computes><persistable>:`
* @editable

`X<native><public>:int = external {}`

* @editable

`Y<native><public>:int = external {}`

* Returns the dot product of `V1` and `V2`. `DotProduct<public>(V1:vector2i, V2:vector2i)<computes>:int = external {}`
* Makes a `vector2i` that is component-wise equal to `V1` and `V2`.
* Fails if any component of `V1` does not equal the corresponding component of `V2`. `Equals<public>(V1:vector2i, V2:vector2i)<computes><decides>:vector2i = external {}`
* Makes a `string` representation of `V`. `ToString<native><public>(V:vector2i)<computes>:string`
* Makes a `vector2i` by component-wise truncation of `V` to `ints`s. `ToVector2i<public>(V:vector2)<varies><decides>:vector2i = external {}`
* Makes a `vector2i` by inverting the signs of `Operand`. `prefix'-'<public>(Operand:vector2i)<computes>:vector2i = external {}`
* Makes a `vector2i` by component-wise addition of `Left` and `Right`. `operator'+'<public>(Left:vector2i, Right:vector2i)<computes>:vector2i = external {}`
* Makes a `vector2i` by component-wise subtraction of `Right` from `Left`. `operator'-'<public>(Left:vector2i, Right:vector2i)<computes>:vector2i = external {}`
* Makes a `vector2i` by multiplying the components of `Left` by `Right`. `operator'*'<public>(Left:vector2i, Right:int)<computes>:vector2i = external {}`
* Makes a `vector2i` by multiplying the components of `Right` by `Left`. `operator'*'<public>(Left:int, Right:vector2i)<computes>:vector2i = external {}`
* 3-dimensional vector with `float` components. `vector3<native><public> := struct<concrete><computes><persistable>:`
* @editable

`X<native><public>:float = external {}`

* @editable

`Y<native><public>:float = external {}`

* @editable

`Z<native><public>:float = external {}`

* Fails if `not SurfaceNormal.MakeUnitVector[]`.

`ReflectVector<native><public>(Direction:vector3, SurfaceNormal:vector3)<varies><decides>:vector3`

* Returns the dot product of `V1` and `V2`. `DotProduct<native><public>(V1:vector3, V2:vector3)<varies>:float`
* Returns the cross product of `V1` and `V2`. `CrossProduct<native><public>(V1:vector3, V2:vector3)<varies>:vector3`
* Returns the Euclidean distance between `V1` and `V2`. `Distance<native><public>(V1:vector3, V2:vector3)<varies>:float`
* Returns the squared Euclidean distance between `V1` and `V2`. `DistanceSquared<native><public>(V1:vector3, V2:vector3)<varies>:float`
* Returns the 2-D Euclidean distance between `V1` and `V2` by ignoring the difference in `Z`. `DistanceXY<native><public>(V1:vector3, V2:vector3)<varies>:float`
* Returns the squared 2-D Euclidean distance between `V1` and `V2` by ignoring their difference in `Z`. `DistanceSquaredXY<native><public>(V1:vector3, V2:vector3)<varies>:float`
* Makes a unit length `vector3` pointing in the same direction of `V`.
* Fails if `V.IsAlmostZero[] or not V.IsFinite[]`. `(V:vector3).MakeUnitVector<native><public>()<varies><decides>:vector3`
* Makes a `string` representation of `V`. `ToString<native><public>(V:vector3)<varies>:string`
* Returns the length of `V`. `(V:vector3).Length<public>()<varies>:float = external {}`
* Returns the squared length of `V`. `(V:vector3).LengthSquared<public>()<computes>:float = external {}`
* Returns the length of `V` as if `V.Z = 0.0`. `(V:vector3).LengthXY<public>()<varies>:float = external {}`
* Returns the squared length of `V` as if `V.Z = 0.0`. `(V:vector3).LengthSquaredXY<public>()<varies>:float = external {}`
* Used to linearly interpolate/extrapolate between `From` (when `Parameter = 0.0`) and `To` (when `Parameter = 1.0`). Expects that all arguments are finite.
* Returns `From*(1 - Parameter) + To*Parameter`. `Lerp<public>(From:vector3, To:vector3, Parameter:float)<varies>:vector3 = external {}`
* Makes a `vector3` by inverting the signs of `Operand`. `prefix'-'<public>(Operand:vector3)<computes>:vector3 = external {}`
* Makes a `vector3` by component-wise addition of `Left` and `Right`. `operator'+'<public>(Left:vector3, Right:vector3)<computes>:vector3 = external {}`
* Makes a `vector3` by component-wise subtraction of `Right` from `Left`. `operator'-'<public>(Left:vector3, Right:vector3)<computes>:vector3 = external {}`
* Makes a `vector3` by component-wise multiplication of `Left` and `Right`. `operator'*'<public>(Left:vector3, Right:vector3)<computes>:vector3 = external {}`
* Makes a `vector3` by multiplying the components of `Left` by `Right`. `operator'*'<public>(Left:vector3, Right:float)<computes>:vector3 = external {}`
* Makes a `vector3` by multiplying the components of `Right` by `Left`. `operator'*'<public>(Left:float, Right:vector3)<computes>:vector3 = external {}`
* Makes a `vector3` by dividing the components of `Left` by `Right`. `operator'/'<public>(Left:vector3, Right:float)<computes>:vector3 = external {}`
* Makes a `vector3` by component-wise division of `Left` by `Right`. `operator'/'<public>(Left:vector3, Right:vector3)<computes>:vector3 = external {}`
* Returns `V` if all components are finite.
* Fails if any of the components are not finite. `(V:vector3).IsFinite<public>()<computes><decides>:vector3 = external {}`
* Succeeds when each component of `V` is within `AbsoluteTolerance` of `0.0`. `(V:vector3).IsAlmostZero<public>(AbsoluteTolerance:float)<computes><decides>:void = external {}`
* Succeeds when each component of `V1` and `V2` are within `AbsoluteTolerance` of each other. `IsAlmostEqual<public>(V1:vector3, V2:vector3, AbsoluteTolerance:float)<computes><decides>:void = external {}`
