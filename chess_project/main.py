import tkinter
import customtkinter
from PIL import Image

# set the appearance
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

# creating the window
width = 900
height = 600
root = customtkinter.CTk()
root.geometry(f"{width}x{height}")
root.title("Chess game")

# declaring the checkbox variables for board
check_box_one_variable_board = tkinter.IntVar()
check_box_one_variable_board.set(1)
check_box_two_variable_board = tkinter.IntVar()
check_box_two_variable_board.set(0)
check_box_three_variable_board = tkinter.IntVar()
check_box_three_variable_board.set(0)

check_box_one_variable_figures = tkinter.IntVar()
check_box_one_variable_figures.set(1)
check_box_two_variable_figures = tkinter.IntVar()
check_box_two_variable_figures.set(0)
check_box_three_variable_figures = tkinter.IntVar()
check_box_three_variable_figures.set(0)


# creating the frames
frame_menu = customtkinter.CTkFrame(master=root,
                                    width=width,
                                    height=height
                                    )
frame_menu.grid(row=0, column=0)

frame_figures = customtkinter.CTkFrame(master=root,
                                       width=width,
                                       height=height
                                       )
frame_figures.grid(row=0, column=0)

frame_board = customtkinter.CTkFrame(master=root,
                                     width=width,
                                     height=height
                                     )
frame_board.grid(row=0, column=0)


# functions for the buttons
def play_menu_frame():
    print("Play")


# menu frame
def create_menu_frame():
    frame_menu.tkraise()

    button1_menu = customtkinter.CTkButton(
        frame_menu,
        text="Play",
        corner_radius=8,
        height=45,
        width=250,
        font=("Cosmic Sans", 23),
        command=play_menu_frame
    )
    button1_menu.place(x=320, y=100)

    # change figures button
    button2_menu = customtkinter.CTkButton(
        frame_menu,
        text="Figures",
        corner_radius=8,
        height=45,
        width=250,
        font=("Cosmic Sans", 23),
        command=create_figures_frame
    )
    button2_menu.place(x=320, y=200)

    # change board button
    button3_menu = customtkinter.CTkButton(
        frame_menu,
        text="Board",
        corner_radius=8,
        height=45,
        width=250,
        font=("Cosmic Sans", 23),
        command=create_board_frame
    )
    button3_menu.place(x=320, y=300)

    # exit button
    button4_menu = customtkinter.CTkButton(
        frame_menu,
        text="Exit",
        corner_radius=8,
        height=45,
        width=250,
        font=("Aerial", 23),
        command=root.quit
    )
    button4_menu.place(x=320, y=400)


# figure frame
def create_figures_frame():
    # functions for the different figures
    def change_board_to_one():
        check_box_two_variable_figures.set(0)
        check_box_three_variable_figures.set(0)
        check_box_figures_one.configure(state="disable")
        check_box_figures_two.configure(state="normal")
        check_box_figures_three.configure(state="normal")

    def change_board_to_two():
        check_box_one_variable_figures.set(0)
        check_box_three_variable_figures.set(0)
        check_box_figures_two.configure(state="disable")
        check_box_figures_one.configure(state="normal")
        check_box_figures_three.configure(state="normal")

    def change_board_to_three():
        check_box_one_variable_figures.set(0)
        check_box_two_variable_figures.set(0)
        check_box_figures_three.configure(state="disable")
        check_box_figures_one.configure(state="normal")
        check_box_figures_two.configure(state="normal")

    # we set this window to be the main window
    frame_figures.tkraise()

    # button for going back to the main menu
    button1_figures = customtkinter.CTkButton(
        frame_figures,
        text="Back to menu",
        corner_radius=8,
        height=45,
        width=200,
        font=("Cosmic Sans", 23),
        command=create_menu_frame
    )
    button1_figures.place(x=20, y=20)

    # label/heading 'Select a figure type'
    label_heading_figures = customtkinter.CTkLabel(frame_figures,
                                                   text="Select a figure type",
                                                   font=("Cosmic Sans", 60))
    label_heading_figures.place(x=205, y=140)

    # making the 'go back to menu' button
    button1_board = customtkinter.CTkButton(
        frame_figures,
        text="Back to menu",
        corner_radius=8,
        height=45,
        width=200,
        font=("Cosmic Sans", 23),
        command=create_menu_frame
    )
    button1_board.place(x=20, y=20)

    # adding all the images
    # adding the first image
    image_one = customtkinter.CTkImage(light_image=Image.open("board_images/board_one_icon.png"),
                                       dark_image=Image.open("board_images/board_one_icon.png"),
                                       size=(90, 90))
    label_one = customtkinter.CTkLabel(frame_figures, text="", image=image_one)
    label_one.place(x=210, y=250)

    # adding the second image
    image_two = customtkinter.CTkImage(light_image=Image.open("board_images/board_two_icon.png"),
                                       dark_image=Image.open("board_images/board_two_icon.png"),
                                       size=(90, 90))
    label_two = customtkinter.CTkLabel(frame_figures, text="", image=image_two)
    label_two.place(x=420, y=250)

    # adding the third image
    image_three = customtkinter.CTkImage(light_image=Image.open("board_images/board_three_icon.png"),
                                         dark_image=Image.open("board_images/board_three_icon.png"),
                                         size=(90, 90))
    label_three = customtkinter.CTkLabel(frame_figures, text="", image=image_three)
    label_three.place(x=630, y=250)

    # adding all the checkboxes for the images
    check_box_figures_one = customtkinter.CTkCheckBox(frame_figures,
                                                      text="",
                                                      variable=check_box_one_variable_figures,
                                                      onvalue=1,
                                                      offvalue=0,
                                                      corner_radius=40,
                                                      command=change_board_to_one
                                                      )
    check_box_figures_one.place(x=243, y=355)

    check_box_figures_two = customtkinter.CTkCheckBox(frame_figures,
                                                      text="",
                                                      variable=check_box_two_variable_figures,
                                                      onvalue=2,
                                                      offvalue=0,
                                                      corner_radius=40,
                                                      command=change_board_to_two
                                                      )
    check_box_figures_two.place(x=453, y=355)

    check_box_figures_three = customtkinter.CTkCheckBox(frame_figures,
                                                        text="",
                                                        variable=check_box_three_variable_figures,
                                                        onvalue=3,
                                                        offvalue=0,
                                                        corner_radius=40,
                                                        command=change_board_to_three
                                                        )
    check_box_figures_three.place(x=663, y=355)

    # we check what is the current figure type, so we call its function
    if check_box_one_variable_figures.get() == 1:
        change_board_to_one()
    elif check_box_two_variable_figures.get() == 2:
        change_board_to_two()
    elif check_box_three_variable_figures.get() == 3:
        change_board_to_three()


# board frame
def create_board_frame():
    # function for changing the board
    def change_board_to_one():
        check_box_two_variable_board.set(0)
        check_box_three_variable_board.set(0)
        check_box_board_one.configure(state="disable")
        check_box_board_two.configure(state="normal")
        check_box_board_three.configure(state="normal")

    def change_board_to_two():
        check_box_one_variable_board.set(0)
        check_box_three_variable_board.set(0)
        check_box_board_two.configure(state="disable")
        check_box_board_one.configure(state="normal")
        check_box_board_three.configure(state="normal")

    def change_board_to_three():
        check_box_one_variable_board.set(0)
        check_box_two_variable_board.set(0)
        check_box_board_three.configure(state="disable")
        check_box_board_one.configure(state="normal")
        check_box_board_two.configure(state="normal")

    # making the main window
    frame_board.tkraise()

    # making the label/heading
    label_heading = customtkinter.CTkLabel(frame_board,
                                           text="Select a board",
                                           font=("Cosmic Sans", 60))
    label_heading.place(x=260, y=140)

    # making the 'go back to menu' button
    button1_board = customtkinter.CTkButton(
        frame_board,
        text="Back to menu",
        corner_radius=8,
        height=45,
        width=200,
        font=("Cosmic Sans", 23),
        command=create_menu_frame
    )
    button1_board.place(x=20, y=20)

    # adding all the images
    # adding the first image
    image_one = customtkinter.CTkImage(light_image=Image.open("board_images/board_one_icon.png"),
                                       dark_image=Image.open("board_images/board_one_icon.png"),
                                       size=(90, 90))
    label_one = customtkinter.CTkLabel(frame_board, text="", image=image_one)
    label_one.place(x=210, y=250)

    # adding the second image
    image_two = customtkinter.CTkImage(light_image=Image.open("board_images/board_two_icon.png"),
                                       dark_image=Image.open("board_images/board_two_icon.png"),
                                       size=(90, 90))
    label_two = customtkinter.CTkLabel(frame_board, text="", image=image_two)
    label_two.place(x=420, y=250)

    # adding the third image
    image_three = customtkinter.CTkImage(light_image=Image.open("board_images/board_three_icon.png"),
                                         dark_image=Image.open("board_images/board_three_icon.png"),
                                         size=(90, 90))
    label_three = customtkinter.CTkLabel(frame_board, text="", image=image_three)
    label_three.place(x=630, y=250)

    # adding all the checkboxes for the images
    check_box_board_one = customtkinter.CTkCheckBox(frame_board,
                                                    text="",
                                                    variable=check_box_one_variable_board,
                                                    onvalue=1,
                                                    offvalue=0,
                                                    corner_radius=40,
                                                    command=change_board_to_one
                                                    )
    check_box_board_one.place(x=243, y=355)

    check_box_board_two = customtkinter.CTkCheckBox(frame_board,
                                                    text="",
                                                    variable=check_box_two_variable_board,
                                                    onvalue=2,
                                                    offvalue=0,
                                                    corner_radius=40,
                                                    command=change_board_to_two
                                                    )
    check_box_board_two.place(x=453, y=355)

    check_box_board_three = customtkinter.CTkCheckBox(frame_board,
                                                      text="",
                                                      variable=check_box_three_variable_board,
                                                      onvalue=3,
                                                      offvalue=0,
                                                      corner_radius=40,
                                                      command=change_board_to_three
                                                      )
    check_box_board_three.place(x=663, y=355)

    if check_box_one_variable_board.get() == 1:
        change_board_to_one()
    elif check_box_two_variable_board.get() == 2:
        change_board_to_two()
    elif check_box_three_variable_board.get() == 3:
        change_board_to_three()


create_menu_frame()

# mainloop
root.mainloop()
