# Housing-Project-in-Mexico
1.1. Organizing Tabular Data in Python

What's Tabular Data?
Information can come in many forms, and part of a data scientist's job is making sure that information is organized in a way that's conducive to analysis. Take for example these five houses from the Mexico real estate dataset we'll use in this project:

Five houses showing price, number of rooms, and area in square meters for each

One common way to organize this information is in a table, which is a group of cells organized into rows and columns:

Table, organized into rows and columns, with housing information from previous image

When working with this sort of tabular data, it's important to organize row and columns following the principles of "tidy data." What does that mean in the case of our dataset?

Each row corresponds to a single house in our dataset. We'll call each of these houses an observation.
Each column corresponds to a characteristic of each house. We'll call these features.
Each cell contains only one value.
Three copies of table from previous image, emphasizing observations as rows and features as columns

So whenever you encounter a new dataset, make sure your data is "tidy."

Tabular Data and Python Data Structures
