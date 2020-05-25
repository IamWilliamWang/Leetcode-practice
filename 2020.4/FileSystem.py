class FileSystem:

    def __init__(self):
        pass
    def ls(self, path: str) -> list:
        return []
    def mkdir(self, path: str) -> None:
        pass
    def addContentToFile(self, filePath: str, content: str) -> None:
        pass
    def readContentFromFile(self, filePath: str) -> str:
        return ''
# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.ls(path)
# obj.mkdir(path)
# obj.addContentToFile(filePath,content)
# param_4 = obj.readContentFromFile(filePath)