# Solar Energy Potential Analysis

## Project Overview

**Theme:** Solar Panel Energy Potential Assessment

This project analyzes solar irradiance maps from the Global Solar Atlas to determine the best locations for solar panel installations. The program processes 10 colour-coded photovoltaic power output maps representing different geographical locations, calculating the energy generation potential (in kWh/kWp) and consistency of each region.

**Data Source:** Images sourced from Global Solar Atlas (https://globalsolaratlas.info/map).

## Visual Feature Detection

### Feature Being Detected
The program detects and quantifies **photovoltaic power output** (kWh/kWp) represented by colour in solar resource maps. Each colour in the image corresponds to a specific kWh/kWp value (ranging from 600 to 2400 kWh/kWp), indicating the annual energy yield per kilowatt-peak of installed solar panel capacity.

**Note:** In this project, the **Feature Density Score** (from `PROJECT.md` list of requirements) is represented by the **Average kWh/kWp** calculated for the region.

### Feature Identification Method
The feature detection works through colour matching:
1. Each pixel's RGB values are compared against a reference colour index
2. The reference maps specific RGB values to kWh/kWp values (photovoltaic power output; Ex. purple/blue = low output 600-900 kWh/kWp, red/orange = high output 1800-2400 kWh/kWp)
3. The program calculates the sum of absolute differences between each individual pixel colour value and the reference colour values
4. The closest matching reference value is assigned to that pixel

### Justification for Detection Accuracy
This colour-based detection method is accurate because:
- **Real-World Data Source:** Images from Global Solar Atlas use standardized colour scales developed by the World Bank Group, ensuring consistent colour-to-energy mapping across all maps
- **Standardized colour Mapping:** Photovoltaic power output maps follow industry-standard colour scales where specific colours directly represent kWh/kWp values
- **Distance-Based Matching:** Using the absolute sum of differences for RGB comparison effectively handles minor colour variations due to compression or display differences
- **Grayscale Filtering:** The program filters out UI elements (legends, borders, labels) by detecting and ignoring grayscale pixels, ensuring only actual data is analyzed
- **Comprehensive Reference Range:** The 19 level colour reference (600-2400 kWh/kWp in 100 kWh/kWp increments) provides sufficient precision for accurate energy detection

### Scientific Basis & References
The Global Solar Atlas uses a standardized colour scale to represent Photovoltaic Power Potential, as documented in the World Bank's 'Global Photovoltaic Power Potential by Country' report. This report confirms that the map colours correspond to specific energy values. The program relies on this established relationship to accurately translate pixel colours into energy potential figures (kWh/kWp), ensuring the analysis is based on real-world data standards.

**Reference:**
https://globalsolaratlas.info/global-pv-potential-study

## Testing and Validation

### Unit Testing
- `getClosestValue()`: Tested with known reference colours to ensure correct kWh/kWp values are returned.
- `isTargetFeature()`: Verified that UI elements with neutral colours (legends, text) are properly filtered.
- `boxBlur()`: Validated that the function correctly smooths image noise by averaging surrounding target pixels while ignoring grayscale UI elements.
- `colourToValue()`: Confirmed that all non-grayscale pixels are processed and converted to kWh/kWp values.
- `nestedArraySelectionSort()`: Validated sorting accuracy for both ascending and descending orders by comparing results with manually sorted data.

### Integration Testing
- Processed all 10 images and verified that:
  - Image blurring effectively minimizes noise and compression artifacts before data extraction, leading to more consistent kWh/kWp averages.
  - Each image produces a reasonable kWh/kWp average based on visual inspection of the colour distribution.
  - Consistency percentages reflect the visual uniformity of each map.
  - Processing times are reasonable.
  - Results align with expected geographic patterns (e.g., regions closer to equator show higher photovoltaic output).

### Edge Cases Handled
- **Noise Isolation:** If a pixel has no surrounding target features, the program retains the original pixel value to prevent data loss.
- **Missing Files:** Implemented error handling for missing image files to prevent runtime crashes.
- **Invalid Input:** Handled invalid user input for kW values and menu selections with default values and retry prompts.

## Code Profiling and Performance Analysis

### Timing Report Example
```
Location 1; Image 1
-----------------------------------------------------------------
You'll average 1504.16 kWh for the region in image 1.
The consistency of the region's kWh is 87.72%
Image 1 processing took 0.667s

...

Total processing time for all images: 21.020s
```

### Performance Analysis
**Slowest Operations:**
1. **Pixel Iteration (nested loops):** The double nested loop iterating through every pixel is the most time-intensive operation. For a typical image with dimensions of ~800×600 pixels, this means ~480,000 iterations per image.

2. **colour Matching (`getClosestValue()`):** For each non-grayscale pixel, the program compares against 19 reference colours, performing RGB distance calculations. This adds additional compute.

3. **Image Blurring (`boxBlur()`):** The blurring process requires calculating the average of surrounding pixels for every data point, adding noticeable computation times per image. (Minor conpared to colour matching, 1 process vs 19 processes)

**Optimization Opportunities:**
- Checking every `x` pixels instead of all could greatly improve performance but compromises accuracy
- Further estimations/generalizations could optimize the colour reference lookup

## Challenges Faced

### Challenge 1: UI Element Interferences
**Problem:** Initial results were inaccurate because the program was analyzing legend colours, borders, and text labels as if they were solar irradiance data.

**Solution:** Implemented the `isTargetFeature()` function to detect and filter neutral-coloured pixels (where R, G, B values are $\pm 10$ units of the average). This effectively removes UI elements while preserving actual coloured data.

### Challenge 2: colour Matching Accuracy
**Problem:** Images from the source had slight colour variations from the reference, making exact RGB matching impossible.

**Solution:** Used sum of absolute RGB differences instead of exact colour matching. This allows the program to find the "closest" reference colour even when pixel colours don't match perfectly.

### Challenge 3: Image Noise and Compression Artifacts
**Problem:** Source images contained compression artifacts and noise (due to screenshotting), which created minor inaccuracies in kWh/kWp readings and reduced the calculated consistency of the regions.

**Solution:** Implemented a selective pixel blur algorithm. The algorithm replaces a pixel's colour with the average of a pixel's neighbours and itself (Ignores UI elements). This colour smoothing prevented noise/artifact pixels from disrupting the data as the inaccurate colour is distributed across several pixels, allowing the colour index estimation algorithm to properly realign all affected pixels to the proper values.
