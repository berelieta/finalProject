var xValue = ['60-69', '70-79', '80-89'];
var yValue = [137, 87, 35];
var trace1 = {
  x: xValue,
  y: yValue,
  type: 'bar',
  hoverinfo: yValue,
  marker: {
    color: "rgb(248,205,221)",
    opacity: 1.0,
    line: {
      color:"rgb(248,205,221)",
      width: 1.5
    }
  }
};
var data = [trace1];
var layout = {
  barmode: 'stack',
  xaxis: {
    title: {
      text: 'Age Group',
      font: {
        family: "Raleway",
        size: 11,
        color: '#7f7f7f'
      }
    },
  },
  yaxis: {
    title: {
      text: 'Number of Positive Cases',
      font: {
        family: "Raleway",
        size: 11,
        color: '#7f7f7f'
      }
    },
  },
};
Plotly.newPlot("canvas", data, layout);


var xValue = ['Almost entirely fatty', 'Extremely dense', 'Heterogeneously Dense', "Scattered Fibroglandular Densities"];
var yValue = [27, 7, 108, 117];
var trace1 = {
  y: yValue,
  type: 'bar',
  textposition: 'bottom',
  text: ['Almost Entirely Fatty', 'Extremely Dense', 'Heterogeneously Dense', 'Scattered Fibroglandular Densities'],
  marker: {
    color: "rgb(248,205,221)",
    opacity: 1.0,
    line: {
      color:"rgb(248,205,221)",
      width: 1.5
    }
  }
};
var data = [trace1];
var layout = {
  barmode: 'stack',
  xaxis: {
    title: {
      text: 'Type of Bi-Rad Diagnosis',
      font: {
        family: "Raleway",
        size: 11,
        color: '#7f7f7f'
      }
    },
  },
  yaxis: {
    title: {
      text: 'Number of Positive Cases',
      font: {
        family: "Raleway",
        size: 11,
        color: '#7f7f7f'
      }
    },
  },
};
Plotly.newPlot("canvas2", data, layout);

var data = [{
  values: [63, 15, 6, 5, 5, 4],
  labels: ["age", "Bi-Rads", "hormone therapy", "family history", "breast biopsy", "mammogram"],
  marker: {
    'colors': [
      "rgb(243, 140, 147)",
      "rgb(246, 156, 169)",
      "rgb(251, 229, 238)",
      "rgb(248, 204, 220)",
      "rgb(251, 229, 238)",
      "rgb(248,205,222)"
    ]
  },
  domain: {column: 0},
  hoverinfo: 'label+percent',
  hole: .4,
  type: 'pie'
}];
var layout = {
  height: 450,
  width: 600,
  showlegend: false,
  grid: {rows: 1, columns: 2}
};
Plotly.newPlot("canvas3", data, layout);