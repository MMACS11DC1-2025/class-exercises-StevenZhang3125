# Mini-Project: Recursive Spiral Staircase 

## **Project Overview**
Draws a spiral staircase (Squares rotated and shrunk on incrementation) 
using a recursive function. Draw method, colour range, and stair depth (square count)
determined by user input.

## **Recursive Approach**
The recursive function `drawSquare` calls itself, adds one, then returns the result. The
terminating/base case triggers when the number of squares left to draw (`remaining`) reaches 0.
Each call draws one square, rotates 5 degrees left, scales the size by 0.99, advances to the next colour in the colour range, and
decreases `remaining` by 1. The function returns the total count of recursive calls made (squares drawn).

## **Configurable Features**

### **Draw Methods**
- **Solid:** Fills each square with colour; creates a spiraling staircase effect
- **Outline:** Outline each square with colour; creating a wireframe spiral effect
### **Colour Range**
- **Reds/Greens/Blues:** Creates a monochromatic range of a colour; allows squares to be distiguished easily whilst still maintaining a general colour tone
- **Rainbow:** Creates a rainbow colour effect; cycles through the rainbow (red, orange, yellow, green, blue, purple) for each square

### **Square Count**
- **Random:**  Generates a random number of squares and displays how many squares were drawn once drawing is complete
- **Random and Guess:** Generates a random number of square and gets the user to guess the number with hints (higher or lower),  
responding with a comment relative to user preformance once correct number is guessed
- **Custom:** User inputs how many square they want drawn (1-250)

## **Usage**
*Note: user inputs have leeway (punctuation, capitalization); unidentifiable inputs allow retries; mismatched variable class causes error*

### How to Run
- Copy and paste code into Trinket compiler (https://trinket.io/turtle) or any other compatible turtle compiler
- Enable fullscreen to avoid cropping

### Draw Method
Input Solid, for each square to be filled  
Input Outline, for each square to only be outlined
### Colour Range
Input Reds, for a colour range of reds  
Input Greens, for a colour range of Greens  
Input Blues, for a colour range of Blues  
Input Rainbow, for a rainbow
### Square Count/Stair Depth
Input 1, for a random depth, displays depth after drawing  
Input 2, for a random depth then guess how many  
Input 3, for a custom depth (1-250)

### Guess (If selected)
Input a number (without counting) and get a hint (higher or lower)  
Input correct number and receive comment dynamic to performance

## **Showcases**
### Example 1
Configuration: Solid, Reds, Random  
Input: `solid`, `reds`, `1`

Output: Red tone spiral staircase with random depth (49)  
Screenshot: ![Example 1](../assets/example-1.png)

### Example 2
Configuration: Outline, Rainbow, Custom: 75  
Input: `outline`, `rainbow`, `3`, `75`

Output: Rainbow spiral staircase/wireframe with depth of 75  
Screenshot: ![Example 2](../assets/example-2.png)

## **Test Cases**
### Test 1: Random count
**Input:** Solid, Reds, Random  
**Expected:** Displays "n squares were drawn." where n is between 10 and 250 inclusive  
**Actual:** Matches expected; displays "129 squares were drawn."  
**Analysis:** Return value matches printed count; recursion terminated correctly.

### Test 2: Random and guess
**Input:** Outline, Rainbow, Random and Guess  
**Expected:** n squares drawn where n is between 10 and 250 inclusive; asked to guess square count; comment relative to performance; displays guesses taken  
**Actual:** Matches expected; displays "Correct! There are 230 squares drawn.", "It took you 5 tries.", "Could be better."  
**Analysis:** Guessing game logic works; dynamic comments based on performance thresholds are correct.

## **Recursion Restrictions and Performance**
### **Recursion Depth Restrictions**
**Too low (<10):** Spiral is very short; very obvious to guess; not visually interesting 

**Reasonable (30-120):** Visually interesting; squares remain visible; balanced performance/fairly fast   

**High (200-250):** New squares are barely visible; pretty pointless/doesn't add much to appearance

### **Performance Implications**
Performance is practically linear to square count; time complexity of about O(n)  

**Low to Medium Count (10-150)**
Squares take some time to be drawn as side lengths are large

**High Count (>200)**
Squares are drawn very quickly but lag may occur as the depth of the recursion consumes considerable memory

### **Suggestion: Reasonable Range**
Anywhere between 30-120 squares is reasonable as it conveys a visually interesting design without causing much performance issues

## **Testing and Debugging Highlights**
### **Issues and Debugging**:
**Colour Selection Error:**  
- Problem: Code was passing entire colour array to `turtle.color()` instead of single colour value
- Solution: Changed from `colours[colour]` to `colours[colour][colourIndex]` to select individual colour from the array
- Result: Colours display properly and iterate through the range

**Fill Mode Not Working:**  
- Problem: Squares not being fill when fill mode was enabled
- Solution: Added `end_fill()` when square was done being drawn; required for each fill and not total filled squares
- Result: Fill/solid mode work properly; fills squares with colour

**Terminating Case Not Working:**  
- Problem: Base case compared sizes which were floats (`size == targetSize`) which would never match exactly due to rounding
- Solution: Replaced with integer countdown (`remaining == 0`) that decreased by 1 every call
- Result: Recursion now terminates after exact number of squares
### **Testing and Validation**
- Verified every combination of prompts and logical responses
- Verified user input error handling (except variable type mismatch errors)

## **Peer Review**
Reviewer: Karson Lum  
Feedback: Confusing instructions for square count selection; Went from word input to number input  
Changes based on feedback: Made selection for square count method expect string responces

*Used as markdown format reference https://markdownguide.offshoot.io/basic-syntax/*