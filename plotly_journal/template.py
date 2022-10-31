import symbol
import plotly.graph_objects as go
import plotly.io as pio

# scatter type
# e.g. A template
template = go.layout.Template()
template.data.scatter = [
    go.Scatter(marker=dict(symbol="diamond", size=10)),
    go.Scatter(marker=dict(symbol="square", size=10)),
    go.Scatter(marker=dict(symbol="circle", size=10))
]

# set template
pio.templates["journal"] = template
