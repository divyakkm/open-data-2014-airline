Analyzing Airline On-Time Data
==================================

<b>Team <br></b>
Divya Menghani <br>
Dheera Prabhakar <br>
Rahul Verma <br>

<b>Introduction</b><br>
As a group, we share common love for air-travel and curiosity about the airline industry. The recent missing Malaysian airline plane related incident spurred our interest further and made us realize how little we know about airlines, their schedules and their function in general. We began researching and stumbled upon US DoT dataset on their website, which looked pretty exhaustive and promising.
The United States Department of Transportation tracks the on-time performance of domestic flights operated by large air carriers. Various airlines have been contributing to the US DoT by sharing their yearly flight data with the U.S. DoT since 1987. The U.S. Department of Transportation publishes a monthly summary of airline on-time performance, including causes of delay, in the Air Travel Consumer Report along with an annual reports on variety of on-time and flight delay data so that the public would have clear information about the nature and sources of airline delays and cancellations.
DoT maintains each year’s data in the form of CSV files. Each file contains on-time arrival data for non-stop domestic flights by major air carriers, and provides such additional items as departure and arrival delays, origin and destination airports, flight numbers, scheduled and actual departure and arrival times, cancelled or diverted flights, taxi-out and taxi-in times, air time, and non-stop distance.
By exploring this dataset, we wanted to understand delay trends in the US airline industry. We planned to find out the most important/popular carriers in the country, evaluate their performance - about delays and the causes for the delays, what cities they affect. Our intent was to unravel some interesting trends in the last few years in the US airline industry with the help of data visualizations.<br>
<b>Problem Statement</b><br>
Our analyses include to find patterns and analyze -
<br><u>1. Delays by Airport</u> - Under this, we calculated the top 20 airports with maximum number of arrival delays and departure delays. We also found out the top 20 airports with maximum average delay in minutes for arrivals and departures. If we had considered data from all the years, we could have made some predictive analysis that could have help users pick an airport with minimal delay in a given city when planning a trip.
<br>2. Delays by Carrier - Calculated the number of cases of arrival and departure delays for all the US carriers of 2008. Likewise, we calculated average delay minutes for carriers for arrivals and departures. Extending this analysis to all years can help users pick the most efficient carrier for their trip.
<br>3. Delays by Route - Calculated the number of cases of arrival and departure delays for all routes and presented a graph with the top 20 routes with maximum number of delays. We then calculated the top 20 airports with high average delay in minutes for arrivals as well as departures. This gives us an idea of what routes are constantly affected by delays. Analyzing the causes of these delays may perhaps reveal links to certain cities being more prone to weather or security delays than others.
<br>4. Delays by age of the plane - Calculated the count of delays and average delays by plane's age. We have top 20 and bottom 20 ages of plane and corresponding to delays.
<br>5. Delays by Day of Time - Calculated the count of delays and average delays by time of the year. We plot a timerseries to understand if specific months or days had more delays as compared to others. We analyzed it for all airports and specifically for SFO airport.
<br>6. Delays by Day of Week - Calculated the count of delays and average delays by day of week. We wanted to find what is the best day to fly by looking at count and average delays.
<br>7. Delays by Day of Month - Calculated the count of delays and average delays by day of month. We wanted to find what is the best day to fly by looking at count and average delays.
<br>8. Busiest airports - We have one map each visualizing the the busiest airports in the US based on the number of flights flying in and out of them. Extending it for all years gives us a sense of how some airports become more (or less) busier over time. This is an indication of increasing population or high trade and tourist activity.
<br>9. Airline route density - We have a map visualization of all possible routes that have been flown over in the US in the year 2008. It gives us a general sense of how connected places in the US are.
<br>10. Top airline routes - Its a map visualization of the top 100 most frequently traveled routes in the US. It gives raises an interesting question of why some routes are busier than others -a possible indication of frequent trading/commercial activity between two cities. Extending our analysis to all the years, we could have seen rise or fall in busyness of certain routes in the US over time. It would raise questions about what would have cause such fluctuations - possible influx of people due to new living opportunities in case of routes that got busier over time
<br><b> About the Data </b><br>
We will be working with airline data for individual years found at http://stat-computing.org/dataexpo/2009/the-data.html. Additionally, we will also be using supplemental data sets about airports, carriers, plane-data found at http://stat-computing.org/dataexpo/2009/supplemental-data.html.
<br><b>Access to Dataset</b><br>
Download the CSV file for any year of your choice from http://stat-computing.org/dataexpo/2009/the-data.html. <br>Place it in you local drive (E.g C:\Users\Admin\Supplemental_data) and assign this path to the variable "INPUT_FILE_PATH" declared under "global constants".<br> Also download the supplemental data and store it in the sample path<br>

<br><b>Challenges</b><br>
Initially, we had planned to consolidate data from all the years to maintain the integrity of our analyses, although we were aware of potential issues arising from processing such large datasets. When we started exploring the datasets with pandas, we realized each file had ~7M rows, which caused substantial processing overhead. We took a step back and decided to restrict our analyses to the most recent year i.e 2008. While working on the project, we got a chance to explore a wide range of choices with respect to data types, python data processing libraries, visualization libraries, mapping libraries etc. Based on tradeoffs related to time, performance, ease of collaboration and the team’s skill level, we have been able to make the right choices and maintain design consistencies.
<br><b>Tools used</b><br>
Python libraries - pandas, numpy, bokeh, seaborn, folium, basemap, pyplot, matplotlib, csv, os
<br>Others - MS Excel
