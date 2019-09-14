library(shiny)
library(shinydashboard)

# Define server logic required 
shinyServer(function(input, output) {

  
  output$volume <- renderPlot({
    
    with(data, plot(data$Date, data$TWTR.Volume, type = "b", main = "Volume Distribution of TWTR", xlab = "Date", ylab = "Volume"))
    })
  
  output$close <- renderPlot({
    
    with(data, plot(data$Date, data$TWTR.Adj.Close, type = "o", main = "Adj Close of TWTR", xlab = "Date", ylab = "Adj Close"))
    
  })
  
  output$close2 <- renderPlot({
    
    with(data, plot(data$Date, data$AMZN.Adj.Close, type = "s", main = "Adj Close of AMZN", xlab = "Date", ylab = "Adj Close"))
    
  })
  
  output$close3 <- renderPlot({
    
    with(data, plot(data$Date, data$GOOG.Adj.Close, type = "l", main = "Adj Close of GOOG", xlab = "Date", ylab = "Adj CLose"))
    
  })
  
  output$chosen <- renderValueBox({
    valueBox("Company Chosen ", input$text_input, icon = icon("eye") )
    
    })
  
  output$type1 <- renderPlot({
    
    with(data2, plot(data2[data2$Company == input$choose_plot,"Date"], data2[data2$Company == input$choose_plot,"Adj.Close"], type = "l", main = paste("Adj Close of ", input$choose_plot), xlab = "Date", ylab = "Adj Close"))
    
  })
  
  output$type2 <- renderPlot({
    
    with(data2, plot(data2[data2$Company == input$choose_plot,"Date"], data2[data2$Company == input$choose_plot,"Volume"], type = "b", main = paste("Volume of ", input$choose_plot), xlab = "Date", ylab = "Volume"))
    
  })
  
  output$type3 <- renderPlot({
    
    hist(data2[data2$Company == input$choose_plot,"Volume"], xlab = "Volume", main = paste("Volume Histogram of ", input$choose_plot))
    
  })
  
  
  output$company <- {(
    renderText(input$comp)
  )}
  
  output$company_all <- renderTable({
    
    print(data[0:6, 0:9])
    
  })
  
  output$summary <- renderPrint({
    summary(data2)
  })
  
   # output$company_sub <- renderTable({
   #   
   #   subset(data_concat, data_concat$Company == input$company_state)
   #   
   # })
  output$company_data_table <- DT::renderDataTable({
    
    data2
  })

  
})
