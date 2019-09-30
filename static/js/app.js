// Plot the default route once the page loads
var defaultURL = "/income";
d3.json(defaultURL).then(function(data) {
  var data = [data];
  var layout = { margin: { t: 30, b: 100 },
                 title: "Income, Unemployment and Crime rates per Ward" 
                };
  Plotly.plot("bar", data, layout);
});

// Update the plot with new data
function updatePlotly(newdata) {
  Plotly.restyle("bar", "x", [newdata.x]);
  Plotly.restyle("bar", "y", [newdata.y]);
}

// Get new data whenever the dropdown selection changes
function getData(route) {
  console.log(route);
  d3.json(`/${route}`).then(function(data) {
    console.log("newdata", data);
    updatePlotly(data);
  });
}

function buildBubbleChart() {

    // @TODO: Use `d3.json` to fetch the sample data for the plots
    var mergedData = "/merged";
      // @TODO: Build a Bubble Chart using the sample data
      d3.json(mergedData).then(function(data){
        var data = [data];
        var layout = {
          title: "Crime vs Economic Status",
          xaxis: {title: "Unemployment (%)"},
          yaxis: {title: "Income"}
        };
        Plotly.newPlot("bubble", data, layout);
});
}

buildBubbleChart()