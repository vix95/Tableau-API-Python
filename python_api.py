import tableauserverclient as TSC

username = "XXX"
password = "XXX"
site_id = "XXX"
server_name = "XXX"


def print_datasources():
    datasources, pagination_item = server.datasources.get()
    print("\nAvailable {} datasources on site:".format(pagination_item.total_available))

    for datasource in datasources:
        print("Name: {0}"
              "\nId: {1}\n".format(datasource.name, datasource.id))


def print_projects():
    project_items, pagination_item = server.projects.get()
    print("\nAvailable {} projects on site:".format(pagination_item.total_available))

    for project in project_items:
        print("Name: {0}"
              "\nId: {1}\n".format(project.name, project.id))


def print_sites():
    sites, pagination_item = server.sites.get()
    print("\nAvailable {} sites on site:".format(pagination_item.total_available))

    for site in sites:
        print("Name: {0}"
              "\nId: {1}"
              "\nContent URL: {2}"
              "\nState: {3}\n".format(site.name, site.id, site.content_url, site.state))


def print_workbooks():
    workbooks, pagination_item = server.workbooks.get()
    print("\nAvailable {} workbooks on site:".format(pagination_item.total_available))

    for workbook in workbooks:
        print("Name: {0}"
              "\nId: {1}\n".format(workbook.name, workbook.id))


def print_views():
    views, pagination_item = server.views.get()
    print("\nAvailable {} views on site:".format(pagination_item.total_available))

    for view in views:
        print("Name: {0}"
              "\nId: {1}\n".format(view.name, view.id))


tableau_auth = TSC.TableauAuth(username=username, password=password, site_id=site_id)
server = TSC.Server("https://" + server_name, use_server_version=True)
print("Server version: {0}".format(server.version))

with server.auth.sign_in(tableau_auth):
    print_datasources()
    print_projects()
    print_sites()
    print_workbooks()
    print_views()

    # Download datasourcres
    # file_path = server.datasources.download('9a9333b1-fa02-4bf4-a6e7-424cc71bc0b2')
    # print("\nDownloaded the file to: {0}.".format(file_path))

    # Download workbooks
    # file_path = server.workbooks.download('700af3d5-1019-4c3b-80a5-5ad9e9f8cb1d')
    # print("\nDownloaded the file to: {0}.".format(file_path))
