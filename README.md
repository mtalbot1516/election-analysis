# election Analysis

## Overview of Project
### The purpose of this election audit analysis was to look at the winning candidate of an election in Colorado using a csv file. Using python through VS code, we discpvered what the total amount of votes were, the breakdown of votes for each candidate and county and the county/Candidate with the most votes. All results were then written to a text file built to hold all election analysis

## Results of Work
* There were 369,711 total votes cast in teh congressional election
* See Resources/county_breakdown.png for county breakdown
* Denver had the largest number of votes
* See Resources/candidate_breakdown for candidate voting breakdown
* Diana Dagette won the congressional election with 272,892 votes. It was 73.8% of the total votes


## Election Audit Summary
### The code is very generalizable for different elections. However, some code will have to change. Specifically, in order to use this code for future elections, you will need to change the source file for the raw data and the text_output file. This is the file_to_load and file_to_save variables. Another way that the code could be changed would be to nest the if statements for county and candidate to get the breakdown by county by candidate.