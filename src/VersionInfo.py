# src/VersionInfo.py

class VersionInfo:
    version = '1.0.0'
    release_date = '2024-07-05'

    @staticmethod
    def get_version() -> str:
        return VersionInfo.version

    @staticmethod
    def get_release_date() -> str:
        return VersionInfo.release_date
