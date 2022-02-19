data = pd.read_csv("BV_QWL_.csv")
data_simp = pd.DataFrame({
    'total_score': data[data.columns[0]],
    'country': data[data.columns[3]],
    'positive_emotion': data[data.columns[22]],
    'engagement': data[data.columns[23]],
    'relationships': data[data.columns[24]],
    'meaning_purpose': data[data.columns[25]],
    'accomplishment': data[data.columns[26]],
    'vitality': data[data.columns[27]],
})

def plot_altair(ymax):
    chart = alt.Chart(data_simp[data_simp['total_score'] < ymax], title = "QWL Overview").mark_bar().encode(
        x = 'country:N',
        y = 'total_score'
    )
    return chart.to_html()

app = Dash(__name__, external_stylesheets=['https://codepen.io/chriddyp/pen/bWLwgP.css'])

app.layout = html.Div([
        html.Iframe(id='bar', 
                    srcDoc=plot_altair(ymax=20),
                    style={'border-width': '0', 'width': '100%', 'height': '500px'}),
        dcc.Slider(id='yslider', min=0, max=40)
])

@app.callback(
    Output('bar', 'srcDoc'),
    Input('yslider', 'value')
)
def update_output(ymax):
    return plot_altair(ymax)

if __name__ == '__main__':
    app.run_server()#debug=True)
