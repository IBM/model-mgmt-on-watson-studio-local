#
# OCO Source Materials
#
# (c) Copyright IBM Corp. 2016
#
# The source code for this program is not published or otherwise divested of
# its trade secrets, irrespective of what has been deposited with the U.S.
# Copyright Office.
#
# File : spark_flights.R
############################################################################


library(dplyr)

# load nycflights13::flights data set
install.packages("nycflights13")
flights_tbl <- copy_to(sc, nycflights13::flights, "flights", overwrite = TRUE)

# load Lahman::Batting data set
install.packages("Lahman")
batting_tbl <- copy_to(sc, Lahman::Batting, "batting", overwrite = TRUE)


# filter by departure delay
flights_tbl %>% filter(dep_delay == 2)

# Using dplyr
delay <- flights_tbl %>%
  group_by(tailnum) %>%
  summarise(count = n(), dist = mean(distance), delay = mean(arr_delay)) %>%
  filter(count > 20, dist < 2000, !is.na(delay)) %>%
  collect()

# plot delays
install.packages("mgcv")
library(ggplot2)
ggplot(delay, aes(dist, delay)) +
  geom_point(aes(size = count), alpha = 1/2) +
  geom_smooth() +
  scale_size_area(max_size = 2)

# Window functions and grouped mutate and filter functions
batting_tbl %>%
  select(playerID, yearID, teamID, G, AB:H) %>%
  arrange(playerID, yearID, teamID) %>%
  group_by(playerID)
