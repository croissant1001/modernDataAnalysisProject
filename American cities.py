import plotly.offline as py
import plotly.graph_objs as go
import plotly.express as px

df = pd.read_csv('2018_USA_city_water_shortage.csv')
df['latitude']=df['City.Location'].str[1:-1].map(lambda x:x.split(',')[0])
df['longitude']=df['City.Location'].str[1:-1].map(lambda x:x.split(',')[1])
df[['latitude','longitude']] = df[['latitude','longitude']].apply(pd.to_numeric)
df.head(5)
#px.set_mapbox_access_token(open(".mapbox_token").read())
token='pk.eyJ1Ijoia2VsbHlzaGllaCIsImEiOiJja25yajVzZTYwMXc4MnB0OWcyaDl1OWJ2In0.UXc7Gx1BGp1C_9K14cj9fA'
map=px.scatter_mapbox(df,
                      lon='longitude',
                      lat='latitude',
                      size='Current.population',
                      color='Magnitude',
                      hover_name='City',
                      hover_data=['City'],
                      size_max=30,
                      color_discrete_sequence=["#636EFA", "#00CC96", "#EF553B"],
                      title="2018 USA Water Shortage Map"
)
map.update_layout(mapbox={'accesstoken':token, 'center':{'lon':-95,'lat':39.7047},'zoom':3.1}
                )

df1 = pd.read_csv('2018_USA_city_water_stress.csv')
df1['latitude']=df1['City.Location'].str[1:-1].map(lambda x:x.split(',')[0])
df1['longitude']=df1['City.Location'].str[1:-1].map(lambda x:x.split(',')[1])
df1[['latitude','longitude']] = df1[['latitude','longitude']].apply(pd.to_numeric)
df1.head(5)
map1=px.scatter_mapbox(df1,
                      lon='longitude',
                      lat='latitude',
                      size='Current.population',
                      color='Magnitude',
                      hover_name='City',
                      hover_data=['City'],
                      size_max=30,
                      color_discrete_sequence=["#636EFA", "#00CC96", "#EF553B"],
                      title="2018 USA Water Stress Map"
)
map1.update_layout(mapbox={'accesstoken':token, 'center':{'lon':-95,'lat':39.7047},'zoom':3.1}
                )