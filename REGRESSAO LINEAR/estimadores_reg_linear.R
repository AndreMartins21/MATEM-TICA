estimate_reg <- function(x, y){
  # Checks if x and y are the same length
  if(length(x) != length(y)){
    cat("\nX: ", length(x), " | Y: ", length(y), "\n\n")
    return("ERRO! Lenght of X is diff from that of Y.")
  } 
  
  sum_x <- sum(x)
  sum_y <- sum(y)
  sum_xy <- sum(x*y)
  sum_x2 <- sum(x^2)
  
  n <- length(x)
  
  b1 <- (n*sum_xy - sum_x*sum_y) / ((n*sum_x2) - (sum_x)^2)
  b1 <- round(b1, 5)
  b0 <- mean(y) - b1*mean(x)
  
  cat("B1: ", b1, "\nB0:", b0)

  return(c(b0, b1))
}

x <- c(1.49, 1.41, 1.65, 1.03, 1.40, 1.10, 1.46, 1.35, 1.17, 0.99)
y <- c(20.8, 18.0, 18.1, 6.0, 18.0, 8.0, 17.5, 12.6, 11.6, 9.2)

b <- estimate_reg(x, y)

# Values compared with the estimated parameters 
# of the native function lm(y~x):
model <- lm(y~x)
summary(model)

