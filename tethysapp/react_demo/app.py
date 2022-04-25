from tethys_sdk.base import TethysAppBase, url_map_maker


class ReactDemo(TethysAppBase):
    """
    Tethys app class for React Demo.
    """

    name = 'React Demo'
    index = 'react_demo:home'
    icon = 'react_demo/images/icon.gif'
    package = 'react_demo'
    root_url = 'react-demo'
    color = '#f39c12'
    description = ''
    tags = ''
    enable_feedback = False
    feedback_emails = []

    def url_maps(self):
        """
        Add controllers
        """
        UrlMap = url_map_maker(self.root_url)

        url_maps = (
            UrlMap(
                name='home',
                url='react-demo',
                controller='react_demo.controllers.home'
            ),
        )

        return url_maps