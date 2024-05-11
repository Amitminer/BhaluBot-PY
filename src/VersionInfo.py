class VersionInfo:
    """
    Represents version information for the application.
    """
    version = '1.0.0'
    release_date = '2024-07-05'

    @staticmethod
    def get_version() -> str:
        """
        Get the current version of the application.
        """
        return VersionInfo.version

    @staticmethod
    def get_release_date() -> str:
        """
        Get the release date of the current version.
        """
        return VersionInfo.release_date
