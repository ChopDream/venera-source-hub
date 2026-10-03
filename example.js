class ExampleSource extends ComicSource {
  name = "示例漫画源";
  key = "example";
  version = "0.1.0";
  minAppVersion = "1.6.0";
  url = "https://raw.githubusercontent.com/ChopDream/venera-source-hub/main/example.js";
  baseUrl = "https://example.com";
  search = { load: async () => { throw "未配置真实站点搜索接口"; } };
  comic = { load: async () => { throw "未配置真实站点详情解析器"; } };
  chapter = { load: async () => { throw "未配置真实站点章节图片解析器"; } };
}
new ExampleSource();
