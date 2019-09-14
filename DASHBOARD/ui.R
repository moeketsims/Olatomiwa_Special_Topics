library(shiny)
library(shinydashboard)
data <- read.csv('C:/Users/Olatomiwa/Documents/SOL PLAATJE UNIVERSITY/HONOURS 2019/2nd Semester/Special Topics/scraped stocks/sp500_All_alt.csv')
data$Date = as.Date(data$Date)

data2 <- read.csv('C:/Users/Olatomiwa/Documents/SOL PLAATJE UNIVERSITY/HONOURS 2019/2nd Semester/Special Topics/scraped stocks/slickcharts/sp500_new2.csv')

#names(subset(data, select=-c(Date)))
#row.names(data) <- data$Date

with(data, plot(data$Date, data$TWTR.Volume, type = "b", main = "Volume Distribution of TWTR", xlab = "Date", ylab = "Volume"))


# Define UI for application
shinyUI(
  dashboardPage( title = "Stock Dashboard",  skin = "black",
    
    dashboardHeader(title = "S&P 500 Dashboard",
                    
                     dropdownMenu(type = "message", 
                                 messageItem(from = "Update", message = "Chief! You're making progress", time = "21:21"),
                                 messageItem(from = "Charts", message = "The charts are looking good fam", icon = icon("bar-chart"), time = "29-08-2019")
                                 ),
                    dropdownMenu(type = "notifications", 
                                 notificationItem(text = "New menu items added", icon = icon("dashboard"), status = "success"),
                                 notificationItem(text = "S & P 500 Loading... Work in progress", icon = icon("warning"), status = "warning")
                                 ),
                    dropdownMenu(type = "tasks", 
                                 taskItem(value = 15, color = "red", "Overall Dashboard Completion"),
                                 taskItem(value = 40, color = "green", "Overall UI Completion"),
                                 taskItem(value = 2, color = "aqua", "Automation")
                                )
                    
                    
                    
                    ),
    
    
    dashboardSidebar(
      
      sidebarMenu(
        
        sidebarSearchForm("searchTest", "buttonSearch", "Search..."),
        
      menuItem("Visualizations", tabName = "Visualizations", icon = icon("image"), badgeLabel = "new", badgeColor = "green"),
      
      menuItem("Detailed Analysis", tabname = "Detailed", icon = icon("bar-chart"),
               
        menuSubItem("Extreme value Theory", tabName = "EVT", icon = icon("line-chart")),
        menuSubItem("Artificial Neural network", tabName = "ANN", icon = icon("clone")),
        menuSubItem("Model", tabName = "model", icon = icon("cogs"))
        
        ),
      
      menuItem("Raw Data", tabName = "Raw", icon = icon("id-card"), badgeLabel = "new", badgeColor = "green"),
      
      radioButtons("comp", "Choose Company", choices = c("AMZN", "TWTR", "PYPL" ), inline = T),
      
      textInput("text_input", "Search Company Name", value = "TWTR")
    
      )
    
    ),
    
    dashboardBody(
      tabItems(
        tabItem(tabName = "Visualizations",
                
                fluidRow(
                  column(width = 12,
                  valueBox(505, "Companies Involved", icon = icon("info-circle"), color = "green"),
                  valueBoxOutput("chosen"))
                ),
                
                fluidRow(
                  box(title = "Volume Plot of TWTR", status = "primary" , solidHeader = T, plotOutput("volume")),
                  box(title = "Adj Close Plot of TWTR", status = "primary", solidHeader = T, plotOutput("close"))
                        ),
                
                fluidRow(
                  tabBox(
                    tabPanel(title = "Adj Close Plot of AMZN", status = "warning", solidHeader = T, plotOutput("close2")),
                    tabPanel(title = "Another Adj Close Plot", status = "warning", solidHeader = T, plotOutput("close3"))
                  ),
                  tabBox(
                    tabPanel(title = "Choose",
                    selectInput("choose_plot",h2("Select Company to Plot"), choices = data2$Company)),
                    tabPanel(title = "Plot type 1", status = "primary", solidHeader = T, plotOutput("type1")),
                    tabPanel(title = "Plot type 2", status = "secondary", solidHeader = T, plotOutput("type2")),
                    tabPanel(title = "Plot type 3", status = "warning", solidHeader = T, plotOutput("type3"))
                  )
                )
                ),
        tabItem(tabname = "Detailed", h1("Detailed Analysis")
                
        
        ),
        tabItem(tabName = "EVT", h1("Extreme Value Theory"),
                fluidRow(
                  box(title = "EVT Distributions", status = "primary" , solidHeader = T, 
                      img(src = 'distribution.png', width = 500, height = 500)
                      ),
                  box(
                    h1("EVT can be classified into 3 major distributions, as the image illustrates"), br(),
                    h1("By choosing the best distribution that fits the data"), br(),
                    h1("Frechet, Gumbell and Weibull distributions ensures that the non normally distributed data is properly analysed")
                  )
                )
        ),
        tabItem(tabName = "ANN", h1("Artificial Neural Network")
                
        ),
        tabItem(tabName = "model", h1("Model")
                
        ),
        tabItem(tabName = "Raw", h1("Raw Data"),
                
                fluidRow(
                  infoBox("Companies Involved", 505, icon = icon("bar-chart-o")),
                  infoBox("Dashboard Level", "Standard", icon = icon("thumbs-up"))
                ),
                
                fluidRow(br(), "Overview of Adj Close & Volume Data: ", br(),
                  tableOutput("company_all")
                ),
                 # fluidRow(
                 #   selectInput("company_state", h2("Select Company Ticker"), choices = data_concat$Company),
                 #   tableOutput("company_sub")
                 # )
                
                tabsetPanel(type = "tab",
                            tabPanel("Data", DT::dataTableOutput("company_data_table")),
                            tabPanel("Summary", verbatimTextOutput("summary"))
                            )
                
                
        )
      

      )
    )
  )
)


