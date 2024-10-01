install.packages("ggplot2")
install.packages("dplyr")
install.packages("statsr")
install.packages("tidyverse")
install.packages("readr")
install.packages("pwr")

library(ggplot2)
library(dplyr)
library(statsr)
library(tidyverse)
library(MASS)
library(pwr)

# Load in already processed dataset
data_path <- "C:/Users/maxme/OneDrive - BUas/Github/2023-24a-fai2-adsai-group-team-media/deliverables/data/processed_data.csv"
data <- read.csv(data_path) %>%
  
  # Keep rows where 'Q2.2' indicates consent
  filter(Q2.2 == "I consent") %>%
  
  # Retain rows with role "Student" or "Educator"
  filter(demo_role %in% c("Student", "Educator")) %>% 
  
  # Create 'year' column based on role and study year
  mutate(year = case_when(
    demo_role == "Student" ~ demo_year_study,
    demo_role == "Educator" ~ "Educator"
  ))

# Filter and count the instances of "Media"
media_count_data <- data %>%
  filter(demo_role == "Student") %>%
  summarise(count = n())

media_count <- media_count_data$count

# Print the result
cat("Number of people who selected 'Media':", media_count)


####################################################################################################################################################
####################################################################################################################################################

# Function to reorder based on negative length
neg_length_order <- function(x) -length(x)

# Total amount of surveyors that finished the questionnaire
# Plot for the total amount of surveyors that finished the questionnaire
plt_finishedsurvey <- ggplot(data, 
                             aes(x = reorder(Finished, Finished, neg_length_order), 
                                 fill = Finished)) +
  geom_bar(width = 0.5) +
  geom_text(aes(label = after_stat(count)), 
            stat = "count", 
            vjust = -1, 
            position = position_dodge(width = 1)) +
  labs(
    title = "Amount of surveyors that finished the questionnaire", 
    x = NULL, 
    y = "Surveyors"
  ) +
  scale_fill_manual(values = c("True" = "#008000", "False" = "#FF0000")) +
  scale_x_discrete(breaks = c("True", "False"), 
                   labels = c("Finished", "Not finished")) +
  theme(
    plot.title = element_text(hjust = 0.5), 
    legend.position = "none"
  ) 

plt_finishedsurvey

# Distribution channels used by surveyor
plt_distributionchannel <- ggplot(data, 
                                  aes(x = reorder(DistributionChannel, DistributionChannel, neg_length_order), 
                                      fill = DistributionChannel)) +
  geom_bar(width = 0.5) +
  geom_text(aes(label = ..count..), 
            stat = "count", 
            vjust = -1, 
            position = position_dodge(width = 1)) +
  labs(
    title = "Distribution channels used by surveyor", 
    x = "Distribution channel", 
    y = "Surveyors"
  ) +
  scale_fill_manual(values=c("qr" = "#D81B60", "anonymous" = "#FFC107")) +
  scale_x_discrete(breaks = c("anonymous", "qr"), 
                   labels = c("Anonymous link", "QR code")) +
  theme(
    plot.title = element_text(hjust = 0.5), 
    legend.position = "none"
  ) 

plt_distributionchannel

# Update unknown sub-domains
data$media_subdomain[data$media_subdomain == ""] <- "Unknown"

# Plot for the sub-domain of the surveyor
plt_subdomain <- ggplot(data, 
                        aes(x = factor(1), 
                            fill = media_subdomain)) +
  geom_bar(width = 1) +
  geom_text(aes(label = ..count..), 
            stat = "count", 
            position = position_stack(vjust = 0.5)) +
  labs(
    title = "Media subdomain of the surveyor", 
    x = NULL, 
    y = NULL
  ) +
  scale_fill_manual(values = c("#D81B60", "#FFC107", "#1E88E5", "#008000", "#6A1B9A")) +
  theme_void() +  # Removing most of the default theme elements
  theme(
    plot.title = element_text(hjust = 0.5)) +
  coord_polar("y")

plt_subdomain

# Plot for the role of the surveyor
plt_role <- ggplot(data, 
                   aes(x = reorder(demo_role, demo_role, neg_length_order), 
                       fill = demo_role)) +
  geom_bar(width = 0.5) +
  geom_text(aes(label = ..count..), 
            stat = "count", 
            vjust = -1, 
            position = position_dodge(width = 1)) +
  labs(
    title = "Role of surveyor", 
    x = element_blank(), 
    y = "Surveyors") +
  scale_fill_manual(values = c("Student" = "#D81B60", 
                               "Educator" = "#FFC107")) +
  theme(
    plot.title = element_text(hjust = 0.5), 
    legend.position = "none"
  )

plt_role

# Plot for the age of the surveyor
plt_age <- ggplot(data, 
                  aes(x = reorder(demo_age, demo_age, neg_length_order), 
                      fill = demo_age)) +
  geom_bar(width = 0.5) +
  geom_text(aes(label = ..count..), 
            stat = "count", 
            vjust = -1, 
            position = position_dodge(width = 1)) +
  labs(
    title = "Age of surveyor", 
    x = element_blank(), 
    y = "Surveyors"
  ) +
  scale_fill_manual(values = c("#D81B60", "#FFC107", "#1E88E5", "#008000", "#6A1B9A")) +
  theme(
    plot.title = element_text(hjust = 0.5), 
    legend.position = "none")

plt_age

# Plot for the gender of the surveyor
plt_gender <- ggplot(data, 
                     aes(x = reorder(demo_gender, demo_gender, neg_length_order), 
                         fill = demo_gender)) +
  geom_bar(width = 0.5) +
  geom_text(aes(label = ..count..), 
            stat = "count", 
            vjust = -1, 
            position = position_dodge(width = 1)) +
  labs(
    title = "Gender of surveyor", 
    x = NULL, 
    y = "Surveyors"
  ) +
  scale_fill_manual(values = c("#D81B60", "#FFC107", "#1E88E5")) +
  theme(
    plot.title = element_text(hjust = 0.5), 
    legend.position = "none")

plt_gender


# Plot for the time surveyor has been working or studying in the media domain
plt_experience_domain <- ggplot(data, 
                                aes(x = reorder(demo_experience, demo_experience, neg_length_order),
                                    fill = demo_experience)) +
  geom_bar(width = 0.5) +
  geom_text(aes(label = ..count..), 
            stat = "count", 
            vjust = -1, 
            position = position_dodge(width = 1)) +
  labs(
    title = "Time surveyor has been working in the media domain", 
    x = NULL, 
    y = "Surveyors"
  ) +
  scale_fill_manual(values = c("#D81B60", "#FFC107", "#1E88E5", "#008000", 
                               "#6A1B9A", "#000080", "#F4A460")) +
  theme(
    plot.title = element_text(hjust = 0.5), 
    legend.position = "none")

plt_experience_domain



####################################################################################################################################################
####################################################################################################################################################


# Define a mapping from survey response numbers to their descriptive labels.
replace_values <- list(
  "1" = "Strongly disagree", 
  "2" = "Somewhat disagree",
  "3" = "Neither agree nor disagree",
  "4" = "Somewhat agree",
  "5" = "Strongly agree"
)

# Function to replace numeric survey responses with their descriptive labels.
# Handles NA values by labeling them as "Unknown".
replace_responses <- function(column) {
  result <- as.character(sapply(column, function(x) {
    if (is.na(x)) {
      "Unknown"
    } else {
      ifelse(is.null(replace_values[[x]]), x, replace_values[[x]])
    }
  }))
  
  factor(
    result, 
    levels = c(
      "Strongly disagree", 
      "Somewhat disagree", 
      "Neither agree nor disagree", 
      "Somewhat agree", 
      "Strongly agree", 
      "Unknown"
    )
  )
}

## Research question 1:
# To what extent do media professionals perceive AI as a tool 
# that enhances their productivity and creativity?

# Work / study experience with AI or AI tools
data$media_experience[data$media_experience == ""] <- "Unknown"

plt_experience <- ggplot(data, aes(
  x = reorder(media_experience, media_experience, neg_length_order),
  fill = media_experience)) +
  geom_bar(width = 0.5) +
  geom_text(
    aes(label = ..count..), 
    stat = "count", 
    vjust = -1, 
    position = position_dodge(width = 1)
  ) +
  labs(
    title = "Work / study experience with AI or AI tools",
    x = NULL,
    y = "Surveyors"
  ) +
  scale_fill_manual(values = c(
    "Unknown" = "#D81B60",
    "less than 1 year" = "#FFC107",
    "1 - 2 years" = "#1E88E5",
    "3 - 4 years" = "#008000"
  )) +
  theme(
    plot.title = element_text(hjust = 0.5), 
    legend.position = "none"
  )

plt_experience


# AI knowledge of surveyor

# Convert media_knowledge_5 column to character to replace NAs with "Unknown"
data$media_knowledge_5 <- as.character(data$media_knowledge_5)
data$media_knowledge_5[is.na(data$media_knowledge_5)] <- "Unknown"

# Use the replace_responses function to update the column
data$media_knowledge_5 <- replace_responses(data$media_knowledge_5)

# Create the plot
plt_experience <- ggplot(data, aes(x = media_knowledge_5, fill = media_knowledge_5)) +
  geom_bar(width = 0.5) +
  geom_text(
    aes(label = ..count..), 
    stat = "count", vjust = -1,
    position = position_dodge(width = 1)
  ) +
  labs(
    title = "AI knowledge of surveyor", 
    x = "Response", 
    y = "Surveyors"
  ) +
  scale_fill_manual(values = c(
    "Strongly disagree" = "#D81B60",
    "Somewhat disagree" = "#FFC107",
    "Neither agree nor disagree" = "#1E88E5",
    "Somewhat agree" = "#008000",
    "Strongly agree" = "#6A1B9A",
    "Unknown" = "#7F8C8D"
  )) +
  theme(
    plot.title = element_text(hjust = 0.5),
    axis.text.x = element_text(angle = 45, hjust = 1)
  )

plt_experience

# Experience working with ChatGPT / BingAI
# Convert to factor and include 'Unknown' as a possible level
data$media_knowledge_6 <- as.character(data$media_knowledge_6)
data$media_knowledge_6[is.na(data$media_knowledge_6)] <- "Unknown"

# Use the replace_responses function to update the column
data$media_knowledge_6 <- replace_responses(data$media_knowledge_6)

# Create the plot
plt_experience <- ggplot(data, aes(x = media_knowledge_6, fill = media_knowledge_6)) +
  geom_bar(width = 0.5) +
  geom_text(
    aes(label = ..count..), 
    stat = "count", vjust = -1,
    position = position_dodge(width = 1)
  ) +
  labs(
    title = "I have experience working with ChatGPT/ BingAI", 
    x = "Response", 
    y = "Surveyors"
  ) +
  scale_fill_manual(values = c(
    "Strongly disagree" = "#D81B60",
    "Somewhat disagree" = "#FFC107",
    "Neither agree nor disagree" = "#1E88E5",
    "Somewhat agree" = "#008000",
    "Strongly agree" = "#6A1B9A",
    "Unknown" = "#7F8C8D"
  )) +
  theme(
    plot.title = element_text(hjust = 0.5),
    axis.text.x = element_text(angle = 45, hjust = 1)
  )

plt_experience

# Surveyor often using AI in daily work
# Convert media_domain_6 column to character to replace NAs with "Unknown"
data$media_domain_6 <- as.character(data$media_domain_6)
data$media_domain_6[is.na(data$media_domain_6)] <- "Unknown"

# Use the replace_responses function to update the column
data$media_domain_6 <- replace_responses(data$media_domain_6)

# Create the plot
plt_experience <- ggplot(data, aes(x = media_domain_6, fill = media_domain_6)) +
  geom_bar(width = 0.5) +
  geom_text(
    aes(label = ..count..), 
    stat = "count", 
    vjust = -1,
    position = position_dodge(width = 1)
  ) +
  labs(
    title = "I often use AI in my daily work", 
    x = "Response", 
    y = "Surveyors"
  ) +
  scale_fill_manual(values = c(
    "Strongly disagree" = "#D81B60",
    "Somewhat disagree" = "#FFC107",
    "Neither agree nor disagree" = "#1E88E5",
    "Somewhat agree" = "#008000",
    "Strongly agree" = "#6A1B9A",
    "Unknown" = "#7F8C8D"
  )) +
  theme(
    plot.title = element_text(hjust = 0.5),
    axis.text.x = element_text(angle = 45, hjust = 1)
  )

plt_experience

####################################################################################################################################################
####################################################################################################################################################

## Research question 2:
# What is the difference between lecturers, 1st and 2nd year students, 
# and 3rd and 4th year students of the perceived impact of AI tools on the quality 
# of content produced in media production and distribution processes?

recode_years <- function(df) {
  df %>% 
    mutate(
      year = recode(
        year,
        'Year 1' = 'Year 1-2',
        'Year 2' = 'Year 1-2',
        'Year 3' = 'Year 3-4',
        'Year 4 (or more)' = 'Year 3-4'
      )
    )
}

data_filtered_domain_7 <- data %>%
  drop_na(year, media_domain_7) %>%
  recode_years() %>%
  filter(year != "Master Student")

data_plot <- ggplot(data = data_filtered_domain_7, aes(x = year, y = media_domain_7)) + 
  geom_boxplot() + 
  ylab("")

print(data_plot)

data_filtered_domain_7 %>%
  inference(
    y = media_domain_7, 
    x = year, 
    statistic = "mean",
    method = "theoretical", 
    type = "ht", 
    alternative = "greater", 
    conf_level = 0.99
  )

####################################################################################################################################################

data_filtered_development_4 <- data %>%
  drop_na(year, media_development_4) %>%
  recode_years() %>%
  filter(year != "Master Student")

ggplot(data = data_filtered_development_4, aes(x=year, y=media_development_4)) + 
  geom_boxplot() + 
  ylab("")

data_filtered_development_4 %>% 
  inference(
    y = media_development_4, 
    x = year, 
    statistic = "mean",
    method = "theoretical", 
    type="ht", 
    alternative="greater", 
    conf_level=0.99
  )

####################################################################################################################################################

data_filtered_development_5 <- data %>%
  drop_na(year, media_development_5) %>%
  recode_years() %>%
  filter(year != "Master Student")

ggplot(data = data_filtered_development_5, aes(x=year, y=media_development_5)) + 
  geom_boxplot() + 
  ylab("")

data_filtered_development_5 %>% 
  inference(
    y = media_development_5, 
    x = year, 
    statistic = "mean",
    method = "theoretical", 
    type="ht", 
    alternative="greater", 
    conf_level=0.99
  )

####################################################################################################################################################

data_filtered_sp_2 <- data %>%
  drop_na(year, media_sp_2) %>%
  recode_years() %>%
  filter(year != "Master Student")

ggplot(data = data_filtered_sp_2, aes(x=year, y=media_sp_2)) + 
  geom_boxplot() + 
  ylab("")

data_filtered_sp_2 %>% 
  inference(
    y = media_sp_2, 
    x = year, 
    statistic = "mean",
    method = "theoretical", 
    type="ht", 
    alternative="greater", 
    conf_level=0.99
  )

####################################################################################################################################################
####################################################################################################################################################
  
## Research question 3
# What factors significantly predict the perceived impact of AI on the 
# quality of content produced in media studies programs?

# Filter out NA values
data_lm_without_na <- data %>%
  drop_na(media_domain_5, media_sp_4)

# Display the dimensions and summarise NA values
dim(data_lm_without_na)
data_lm_without_na %>% 
  summarise_all(~ sum(is.na(.)))

# Convert to numeric
data_lm_without_na$media_sp_2 <- as.numeric(as.character(data_lm_without_na$media_sp_2))
data_lm_without_na$media_knowledge_7 <- as.numeric(as.character(data_lm_without_na$media_knowledge_7))

# Calculate correlations
cor(data_lm_without_na$media_sp_2, data_lm_without_na$media_knowledge_7)
cor(data_lm_without_na$media_sp_2, data_lm_without_na$media_trust_1)
cor(data_lm_without_na$media_domain_5, data_lm_without_na$media_sp_4)

# Scatter plot functions
scatter_plot <- function(data, x_var, y_var) {
  ggplot(data, aes(x = .data[[x_var]], y = .data[[y_var]])) +
    geom_point() +
    stat_smooth(method = "lm", se = FALSE)
}

print(scatter_plot(data_lm_without_na, "media_knowledge_7", "media_sp_2"))
print(scatter_plot(data_lm_without_na, "media_trust_1", "media_sp_2"))
print(scatter_plot(data_lm_without_na, "media_domain_5", "media_sp_4"))

# Linear model and summary
lml <- lm(data = data_lm_without_na, formula = media_sp_4 ~ media_domain_5)
summary(lml)

# Residual plots
print(ggplot(lml, aes(x = .fitted, y = .resid)) +
        geom_point() +
        geom_hline(yintercept = 0, linetype = "dashed") +
        xlab("Fitted values") +
        ylab("Residuals"))

print(ggplot(lml, aes(x = .resid)) +
        geom_histogram(bins = 20) +
        xlab("Residuals"))

print(ggplot(lml, aes(sample = .resid)) +
        stat_qq() + 
        stat_qq_line(col = 'blue', lty = "longdash", linewidth = 1) +
        xlab("Theoretical") + ylab("Sample"))

# Box-Cox transformation
b <- boxcox(lml)
lambda <- b$x[which.max(b$y)]
data_lm_without_na <- data_lm_without_na %>% 
  mutate(media_sp_4_trans = (media_sp_4 ^ lambda - 1) / lambda)

# Adjusted model and plots
lm2 <- lm(data = data_lm_without_na, formula = media_sp_4_trans ~ media_domain_5)

print(ggplot(lm2, aes(sample = .resid)) +
        stat_qq() + stat_qq_line(col = 'blue', lty = "longdash", linewidth = 1) +
        xlab("Theoretical") + ylab("Sample"))

print(ggplot(lm2, aes(x = .resid)) +
        geom_histogram(bins = 20) +
        xlab("Residuals"))

# Shapiro-Wilk test
shapiro.test(lm2$residuals)

# Power analysis
f2_effect_size = 0.15
n = 92
p = 1

# Conducting the power analysis
pwr.f2.test(u = p, 
            v = n - p - 1, 
            f2 = f2_effect_size, 
            sig.level = 0.05, 
            power = NULL)

