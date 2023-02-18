import django_tables2 as tables
from .models import DataTable

class ReviewTable(tables.Table):
    class Meta:
        model = DataTable
        template_name = "django_tables2/bootstrap.html"
        fields = ("Sentiment", "L1_Cluster_ID", "L1_Cluster", "L1_PhraseCount", "L1_ReviewCount", "L1_RatingPhrase", "L1_RatingReview", "L2_Cluster_ID", "L2_Cluster", "L2_PhraseCount", "L2_ReviewCount", "L2_RatingPhrase", "L2_RatingReview", "L3_Cluster_ID", "L3_Cluster", "L3_ClusterPhrase", "L3_PhraseCount", "L3_ReviewCount", "L3_RatingPhrase", "L3_RatingReview", "L4_ID", "L4_Phrase", "review_id", "reviewRating", "review", "reviewDate", "flag", "ReviewRow_id")