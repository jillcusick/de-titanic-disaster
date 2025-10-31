# Load packages
library(tidyverse)
library(caret)

cat("Loaded packages: tidyverse and caret.\n")

# Load training data
train_df <- read_csv("src/data/train.csv")
cat("Loaded train.csv.\n")

# View data
print(head(train_df))
cat("Viewing data...\n")

# Keep only variables needed for prediction
train_df_sub <- train_df %>% select(Survived, Pclass, Sex, Age, Fare)
cat("Filtered to variables: Survived, Pclass, Sex, Age, Fare.\n")

# Check missing values
print(colSums(is.na(train_df_sub)))
cat("Checked missing values.\n")

# Impute missing Age with median
train_df_sub$Age[is.na(train_df_sub$Age)] <- median(train_df_sub$Age, na.rm = TRUE)
cat("Imputed missing Age values.\n")

# Encode 'Sex' as numeric
train_df_sub$Sex <- as.factor(train_df_sub$Sex)
train_df_sub$Sex <- as.numeric(train_df_sub$Sex) - 1
cat("Encoded 'Sex' as numeric.\n")

# Build logistic regression model
x_train <- train_df_sub %>% select(-Survived)
y_train <- train_df_sub$Survived

model <- glm(Survived ~ ., data = train_df_sub, family = binomial)
cat("Logistic regression model trained.\n")

# Predict on training set
train_preds <- predict(model, x_train, type = "response")
train_preds_class <- ifelse(train_preds > 0.5, 1, 0)
train_acc <- mean(train_preds_class == y_train)
cat(sprintf("Training accuracy: %.4f\n", train_acc))

# Load test data
test_df <- read_csv("src/data/test.csv")
cat("Loaded test.csv.\n")

# Filter to same prediction variables
test_df_sub <- test_df %>% select(Pclass, Sex, Age, Fare)

# Impute missing Age and Fare
test_df_sub$Age[is.na(test_df_sub$Age)] <- median(test_df_sub$Age, na.rm = TRUE)
test_df_sub$Fare[is.na(test_df_sub$Fare)] <- median(test_df_sub$Fare, na.rm = TRUE)
cat("Imputed missing Age and Fare values.\n")

# Encode 'Sex' as numeric
test_df_sub$Sex <- as.factor(test_df_sub$Sex)
test_df_sub$Sex <- as.numeric(test_df_sub$Sex) - 1
cat("Encoded 'Sex' as numeric.\n")

# Predict on test set
test_preds <- predict(model, test_df_sub, type = "response")
test_preds_class <- ifelse(test_preds > 0.5, 1, 0)
cat("Predictions on test set complete.\n")

# Combine with PassengerId
output_df <- tibble(
  PassengerId = test_df$PassengerId,
  Survived = test_preds_class
)

# Save predictions
write_csv(output_df, "src/test_predictions_R.csv")
cat("Predictions saved to src/test_predictions_R.csv.\n")