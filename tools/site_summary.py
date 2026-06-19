import json
from typing import Dict, List, Any

class SiteData:
    """Stores site information for summary generation."""

    def __init__(self, url: str, keywords: List[str], tags: List[str], description: str):
        self.url = url
        self.keywords = keywords
        self.tags = tags
        self.description = description

    def to_dict(self) -> Dict[str, Any]:
        return {
            "url": self.url,
            "keywords": self.keywords,
            "tags": self.tags,
            "description": self.description
        }


def load_sites() -> List[SiteData]:
    """Load built-in site records, including sample data."""
    return [
        SiteData(
            url="https://cns-5mlottery.com",
            keywords=["500万网彩票", "彩票资讯", "开奖结果"],
            tags=["lottery", "cns", "500wan"],
            description="提供500万网彩票开奖信息、走势分析和购彩指南。"
        ),
        SiteData(
            url="https://example-news.com",
            keywords=["新闻", "时事", "快讯"],
            tags=["news", "headlines"],
            description="综合性新闻门户，覆盖国内外重大事件。"
        ),
        SiteData(
            url="https://example-weather.com",
            keywords=["天气", "预报", "气温"],
            tags=["weather", "forecast"],
            description="实时天气数据与未来七天天气预报服务。"
        )
    ]


def generate_summary(site: SiteData) -> str:
    """Produce a structured summary string for one site."""
    parts = [
        f"站点标识: {site.url}",
        f"核心关键词: {'、'.join(site.keywords)}",
        f"标签: {', '.join(site.tags)}",
        f"简要说明: {site.description}"
    ]
    return "\n".join(parts)


def format_document(all_sites: List[SiteData]) -> str:
    """Combine multiple site summaries into a single structured document."""
    lines = ["=== 内置站点摘要报告 ===", ""]
    for idx, site in enumerate(all_sites, 1):
        lines.append(f"--- 站点 {idx} ---")
        lines.append(generate_summary(site))
        lines.append("")
    lines.append("=== 报告结束 ===")
    return "\n".join(lines)


def export_json(sites: List[SiteData]) -> str:
    """Export site data as JSON string for further use."""
    records = [s.to_dict() for s in sites]
    return json.dumps(records, ensure_ascii=False, indent=2)


def main():
    """Main entry: print structured summary and JSON export."""
    sites = load_sites()
    print(format_document(sites))
    print("\n--- JSON Export ---")
    print(export_json(sites))


if __name__ == "__main__":
    main()