
# Mole Game
## CS110 Final Project  Fall, 2023

## Team Members

Jayden Posner, Ryan Kurtz
***

## Project Description

User will have to click on moles before they dissapear. For each mole that is clicked, one point is added to the user's score. If the user ends with more than 10 points, they win, if else they lose
***    

## GUI Design

### Initial Design

![initial gui](assets/gui.jpg)

### Final Design

![final gui](assets/finalgui.jpg)

## Program Design

### Features

1. Scoring System
2. Results screen
3. Custom icons
4. Multiple progressive rounds
5. Leaderboard

### Classes

- << You should have a list of each of your classes with a description >>

## ATP

Test Case 1: Menu goes into game
-Test Description: Verifies that the menu transitions properly
-Test Steps:
    1. Start The Game
    2. Click the Space bar
    3. Verify that the game starts
-Expected Outcome: Clicking space should start the game

Test Case 2: Explination screen
-Test Description: Verifies that the explination screen can be shown and exited
-Test Steps:
    1. Start The Game
    2. Click e
    3. Verify than an explination for the game is displayed
    4. Click e or space
    5. Verify that you are returned to the menu screen
-Expected Outcome: The player is able to navigate to the explination screen and back

Test Case 3: Collision
-Test Description: Ensures that clicking the mouse on a sprite is detected
-Test Steps:
    1. Start the game
    2. Click space
    3. Mouse click on the mole image
    4. Verify that the program reacts by moving the image
-Expected Outcome: The program recognizes a collision when the mouse is clicked

Test Case 4: Game Over
-Test Description: Show that the game transitions to the end screen
-Test Steps:
    1. Start the game
    2. click space
    3. wait
    4. Verify that the game over screen appears
-Expected Outcome: The game should display the game over screen after all 10 moles have appeared and dissapeared

Test Case 5: Incorrect Inputs
-Test Description: Show that the program doesn't react to incorrect input
-Test Steps:
    1. Start the game
    2. Click any key or mouse button that isn't space or e
    3. Verify that nothing changes
    4. Click space
    5. Verify that clickng any key does not lead to any change in the mole sprite
-Expected Outcome: The program doesn't crash with incorrect input and the program doesn't allow incorrect input to change the outcome of the program

    















    















