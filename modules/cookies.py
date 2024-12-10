from yt_dlp import YoutubeDL

def save_cookies_from_chrome(output_file='cookies.txt'):
    # 配置选项
    ydl_opts = {
        'cookiefile': output_file,  # 指定输出的 cookie 文件
        'cookiesfrombrowser': ('chrome',),  # 从 Chrome 浏览器获取 cookies
    }
    
    # 创建下载器实例
    with YoutubeDL(ydl_opts) as ydl:
        try:
            # 这里使用一个虚拟的 URL 来触发 cookies 保存
            ydl.extract_info('https://www.youtube.com', download=False)
            print(f"Cookies 已保存到 {output_file}")
        except Exception as e:
            print(f"保存 cookies 出错: {str(e)}")

# 示例调用
if __name__ == "__main__":
    save_cookies_from_chrome()