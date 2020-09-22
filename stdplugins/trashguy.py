# =================================================== #
#                 Trash Guy Script                    #
#                     (> ^_^)>                        #
#              Made by Zac (t.me/Zacci)               #
#                 Version 3.2.0-pi                    #
#         Donate:                                     #
#         1CoRm4mKCUPs5XQnFVSVQ4xGMAp29pyYzC          #
# =================================================== #
# Copyright (C) 2019 Zac (https://t.me/Zacci)         #
# Permission is hereby granted, free of charge, to    #
# any person obtaining a copy of this software and    #
# associated documentation files (the "Software"),    #
# to deal in the Software without restriction,        #
# including without limitation the rights to use,     #
# copy, modify, merge, publish, distribute,           #
# sublicense, and/or sell copies of the Software,     #
# and to permit persons to whom the Software is       #
# furnished to do so, subject to the following        #
# conditions: The above copyright notice and this     #
# permission notice shall be included in all copies   #
# or substantial portions of the Software.            #
# =================================================== #
import sys


def main():
    """Example usage of TrashGuy class."""
    # user_input = '🍓 🍅 🍊'
    user_input = " ".join(sys.argv[1:])

    trash_guy = TrashGuy(user_input, symbol_spacing=Symbols.SPACER_EMOJI)

    print(trash_guy)


class Symbols:
    SPACER_DEFAULT = "\u0020"
    SPACER_WIDE = "\u2800\u0020"
    SPACER_EMOJI = "➖"
    DEFAULT_INPUT = "\u2622"
    MONOSPACE_WRAPPER = "`"
    TRASH_EMOJI = "\U0001F5D1"
    GUY_LEFT = "<(^_^ <)"
    GUY_RIGHT = "(> ^_^)>"


class TrashGuy:
    def __init__(
        self,
        user_input: str,
        symbol_trash: str = Symbols.TRASH_EMOJI,
        symbol_left: str = Symbols.GUY_LEFT,
        symbol_right: str = Symbols.GUY_RIGHT,
        symbol_spacing: str = Symbols.SPACER_DEFAULT,
        monospace_wrapper: str = Symbols.MONOSPACE_WRAPPER,
        wrap_monospace: bool = False,
    ):
        if not user_input:
            self.user_input = [Symbols.DEFAULT_INPUT]
        else:
            self.user_input = str(user_input).split()

        self.symbol_trash = symbol_trash
        self.symbol_left = symbol_left
        self.symbol_right = symbol_right
        self.symbol_spacing = symbol_spacing
        self.monospace_wrapper = monospace_wrapper
        self.wrap_monospace = wrap_monospace

    def __str__(self):
        return "\n".join(iter(self))

    def __add(self, frames: list, frame):
        if self.wrap_monospace:
            wrapper = [Symbols.MONOSPACE_WRAPPER]
            frames.append("".join(wrapper + list(frame) + wrapper))
        else:
            frames.append("".join(list(frame)))

    def __iter__(self):
        """Dynamically generated frames of the animated trash guy using provided symbols."""
        trash_item_sequence = []

        trash_input = self.user_input
        trash_length = len(trash_input)
        trash_reversed = reversed(trash_input)

        s_trash = self.symbol_trash
        s_left = self.symbol_left
        s_right = self.symbol_right
        s_space = self.symbol_spacing

        trash_truncator = trash_length
        # The animation is created from right to left and bottom to up and then reversed at each frame step.
        # This means that the code snapshots frames in the opposite order to how they appear in the final animation.
        # This is due to the nature of trash guy picking up items from the left-hand side.
        #
        # The animation is based on this loop which iterates over the user
        # input items.
        for item in trash_reversed:
            truncating_items = trash_input[:trash_truncator]
            truncated_len_difference = trash_length - trash_truncator
            space_padding = [s_space] * truncated_len_difference

            # Create a dynamic canvas while each item disappears
            canvas = [*truncating_items + space_padding, *[s_space] * 3, s_trash]
            r_canvas = list(reversed(canvas))

            last_item_index = -len(truncating_items)
            frames = []
            # Loop over the canvas to animate the trash guy going right while
            # holding the item.
            for index in range(len(r_canvas)):
                # Trash guy hits the item he wants to pickup
                if r_canvas[index] == s_space or -index == last_item_index:
                    try:
                        if r_canvas[index - 1] == s_trash:
                            # Looking left on the very final frame of the
                            # animation
                            r_canvas[index] = s_left

                            # Temporarily remove the item from the trash pile
                            # while trash guy is holding it
                            if r_canvas[last_item_index] == item:
                                r_canvas[last_item_index] = s_space

                            # Snapshot last frame looking left
                            self.__add(frames, reversed(r_canvas))

                            # Set trash guy's previous position
                            r_canvas[index] = s_right

                            # Snapshot before-last frame
                            self.__add(frames, reversed(r_canvas))

                            # Remove trash guy from this position for next frame (which is the previous frame)
                            # (must be set to space character)
                            r_canvas[index] = s_space

                        # Animate trash guy going right with the item until he
                        # hits the trash can
                        elif (
                            r_canvas[index - 1] == s_space
                            and r_canvas[index - 1] != s_trash
                        ):
                            r_canvas[index - 1] = item
                            r_canvas[index] = s_right

                            # Temporarily remove the item from the trash pile
                            # while trash guy is holding it
                            if r_canvas[last_item_index] == item:
                                r_canvas[last_item_index] = s_space

                            # Snapshot frame while moving towards trash can
                            self.__add(frames, reversed(r_canvas))

                            # Clear the last two spaces for the next frame
                            r_canvas[index] = s_space
                            r_canvas[index - 1] = s_space

                    except IndexError:
                        pass  # animation reached end

            # Loop over the canvas to animate trash guy going from the
            # beginning of the animation towards the items
            for index in range(len(canvas)):
                # if the guy is near the trash can, skip the frame
                if canvas[index] == s_space and canvas[index + 1] != s_trash:
                    # animate guy starting from the first space after the one
                    # being next to the trash can
                    canvas[index] = s_left

                    # Snapshot the frames of the animation going left for as
                    # long as there are whitespaces
                    self.__add(frames, canvas)

                    # Remove the previous position and continue
                    canvas[index] = s_space

            # Append all frames in reverse order
            trash_item_sequence += list(reversed(frames))

            # Truncate the items list by one item each loop
            trash_truncator -= 1

        return iter(trash_item_sequence)


if __name__ == "__main__":
    main()
