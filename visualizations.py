"""
Add a map to a Plotly figure
"""


def add_map(fig):
    """
    Add a map to a Plotly plot and displays the resulting figure.

    Assumes an existing Plotly figure.

    Args:
        fig: variable name of the existing figure to add the map to

    Returns:
        None
    """

    fig.update_layout(
        # Set a white background to lay the map onto
        mapbox_style="white-bg",
        mapbox_layers=[
            {
                "below": 'traces',
                # Set map to satellite imagery style
                "sourcetype": "raster",
                "sourceattribution": "United States Geological Survey",
                # Pass the map to use
                "source": [
                    "https://basemap.nationalmap.gov/arcgis/rest/services/\n"
                    "USGSImageryOnly/MapServer/tile/{z}/{y}/{x}"
                ]
            }
        ])
    # Set the map margins
    fig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})
    fig.show()
