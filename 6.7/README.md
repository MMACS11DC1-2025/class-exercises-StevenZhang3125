# Solar Energy Potential Analysis

## Project Overview

**Theme:** Solar Panel Energy Potential Assessment

This project analyzes solar irradiance maps from the Global Solar Atlas to determine the best locations for solar panel installations. The program processes 10 color-coded photovoltaic power output maps representing different geographical locations, calculating the energy generation potential (in kWh/kWp) and consistency of each region.

**Data Source:** Images sourced from Global Solar Atlas (https://globalsolaratlas.info/map), a free, web-based application providing solar resource data globally.

## Visual Feature Detection

### Feature Being Detected
The program detects and quantifies **photovoltaic power output** (kWh/kWp) represented by color in solar resource maps. Each color in the image corresponds to a specific kWh/kWp value (ranging from 600 to 2400 kWh/kWp), indicating the annual energy yield per kilowatt-peak of installed solar panel capacity.

**Note:** In this project, the **Feature Density Score** (from `PROJECT.md` list of requirements) is represented by the **Average kWh/kWp** calculated for the region.

### Feature Identification Method
The feature detection works through color matching:
1. Each pixel's RGB values are compared against a reference color palette
2. The reference maps specific RGB values to kWh/kWp (photovoltaic power output) values (e.g., purple/blue = low output ~600-900 kWh/kWp, red/orange = high output ~1800-2400 kWh/kWp)
3. The program calculates the sum of absolute differences between each individual pixel color value and the reference color values
4. The closest matching reference value is assigned to that pixel

### Justification for Detection Accuracy
This color-based detection method is accurate because:
- **Real-World Data Source:** Images from Global Solar Atlas use standardized color scales developed by the World Bank Group, ensuring consistent color-to-energy mapping across all maps
- **Standardized Color Mapping:** Photovoltaic power output maps follow industry-standard color scales where specific colors directly represent kWh/kWp values
- **Distance-Based Matching:** Using the absolute sum of differences for RGB comparison effectively handles minor color variations due to compression or display differences
- **Grayscale Filtering:** The program filters out UI elements (legends, borders, labels) by detecting and ignoring grayscale pixels, ensuring only actual data is analyzed
- **Comprehensive Reference Range:** The 19-point color reference (600-2400 kWh/kWp in 100 kWh/kWp increments) provides sufficient granularity for accurate energy assessment

## Testing and Validation

### Unit Testing
- `getClosestValue()`: Tested with known reference colors to ensure correct kWh/kWp values are returned
- `isTargetFeature()`: Verified that UI elements with neutral colors (legends, text) are properly filtered
- `colourToValue()`: Confirmed that all non-grayscale pixels are processed and converted to kWh/kWp values
- `nestedArraySelectionSort()`: Validated sorting accuracy by comparing results with manually sorted data

### Integration Testing
- Processed all 10 images and verified that:
  - Each image produces a reasonable kWh/kWp average based on visual inspection of the color distribution
  - Consistency percentages reflect the visual uniformity of each map
  - Processing times are reasonable
  - Results align with expected geographic patterns (e.g., regions closer to equator show higher photovoltaic output)

### Edge Cases Handled
- Missing image files (try and except, preventing runtime errors)
- Invalid user input for kW values (defaults to 1kW)
- Invalid menu selections (permits retries with error/instruction messages)

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

2. **Color Matching (`getClosestValue()`):** For each non-grayscale pixel, the program compares against 19 reference colors, performing RGB distance calculations. This adds additional compute.

3. **Selection Sort:** While functional, Selection Sort has O($n^2$) complexity. However, with only 10 images, sorting time is practically zero.

**Optimization Opportunities:**
- Pre-processing images to lower resolution could reduce pixel count
- Further estimations/generalizations could optimize the color reference lookup

## Challenges Faced

### Challenge 1: UI Element Interferences
**Problem:** Initial results were inaccurate because the program was analyzing legend colors, borders, and text labels as if they were solar irradiance data.

**Solution:** Implemented the `isTargetFeature()` function to detect and filter neutral-colored pixels (where R, G, B values are $\pm 10$ units of the average). This effectively removes UI elements while preserving actual colored data.

### Challenge 2: Color Matching Accuracy
**Problem:** Images from the source had slight color variations from the reference, making exact RGB matching impossible.

**Solution:** Used sum of absolute RGB differences instead of exact color matching. This allows the program to find the "closest" reference color even when pixel colors don't match perfectly.
