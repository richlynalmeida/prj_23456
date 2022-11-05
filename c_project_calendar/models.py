from django.db import models
from a_hr.models import Company


class Project(models.Model):
    project_code = models.CharField(unique=True, max_length=5, verbose_name='Project Code')
    project_title = models.CharField(max_length=55, blank=True, null=True, verbose_name='Project Title')
    venue = models.CharField(max_length=55, blank=True, null=True, verbose_name='Project Venue')
    comments = models.CharField(max_length=2000, blank=True, null=True, verbose_name='Project Comments')
    company = models.ForeignKey(Company, on_delete=models.CASCADE, verbose_name='Company ID')
    start_date = models.DateTimeField(blank=True, null=True, verbose_name='Project Start Date')
    finish_date = models.DateTimeField(blank=True, null=True, verbose_name='Project Finish Date')

    class Meta:
        managed = True
        verbose_name_plural = 'Project'
        db_table = 'project'
        app_label = 'c_project_calendar'
        ordering = ['project_code']

    # def __str__(self):
    #     return str('%s' % self.project_code)
    def __str__(self):
        return f"{self.project_code} - {self.project_title}"


class CameoseDates(models.Model):
    date_code = models.CharField(unique=True, max_length=10, verbose_name='Date Code')
    sole_date = models.DateTimeField(unique=True, verbose_name='Date')
    day_no = models.IntegerField(verbose_name='Day Number of the Month')
    day_no_text = models.CharField(max_length=2, verbose_name='Day Number of the Month - Text')
    day_suffix= models.CharField(max_length=2, verbose_name='Day Suffix for Day Number of the Month')
    day_name_short = models.CharField(max_length=3, verbose_name='Day Name - Short')
    day_name_long = models.CharField(max_length=9, verbose_name='Day Name - Long')
    day_no_of_the_week = models.IntegerField(verbose_name='Day Number of the Week')
    day_no_of_the_week_text = models.CharField(max_length=2, verbose_name='Day Number of the Week - Text')
    day_no_of_the_week_in_month = models.IntegerField(verbose_name='Day Number of the Week in the Month')
    day_no_of_the_week_in_month_text = models.CharField(max_length=2,
                                                        verbose_name='Day Number of the Week in the Month - Text')
    day_no_of_the_year = models.IntegerField(verbose_name='Day Number of the Year')
    day_no_of_the_year_text = models.CharField(max_length=2, verbose_name='Day Number of the Year - Text')
    week_no_of_the_year = models.IntegerField(verbose_name='Week Number of the Year')
    week_no_of_the_year_text = models.CharField(max_length=2, verbose_name='Week Number of the Year - Text')
    week_no_of_the_year_iso = models.IntegerField(verbose_name='Week Number of the Year - ISO')
    week_no_of_the_year_iso_text = models.CharField(max_length=2, verbose_name='Week Number of the Year - ISO - Text')
    week_no_of_the_month = models.IntegerField(verbose_name='Week Number of the Month')
    week_no_of_the_month_text = models.CharField(max_length=2, verbose_name='Week Number of the Month - Text')
    first_date_of_the_week = models.DateTimeField(verbose_name='First Date of the Week')
    last_date_of_the_week = models.DateTimeField(verbose_name='Last Date of the Week')
    month_no = models.IntegerField(verbose_name='Month Number of the Year')
    month_no_text = models.CharField(max_length=2, verbose_name='Month Number of the Year - Text')
    month_name_short = models.CharField(max_length=3, verbose_name='Month Name - Short')
    month_name_long = models.CharField(max_length=9, verbose_name='Month Name - Long')
    is_stat_holiday_usa = models.IntegerField(verbose_name='Statutory Holiday Flag in the USA')
    stat_holiday_name_usa = models.CharField(max_length=55, blank=True, null=True, verbose_name='Statutory Holiday Name in the USA')
    is_stat_holiday_canada = models.IntegerField(verbose_name='Statutory Holiday Flag in Canada')
    stat_holiday_name_canada = models.CharField(max_length=55, blank=True, null=True, verbose_name='Statutory Holiday Name in Canada')
    is_weekend = models.IntegerField(verbose_name='Weekend Flag')
    is_leap_year = models.IntegerField(verbose_name='Leap Year Flag')
    year_with_53_weeks = models.IntegerField(verbose_name='Year with 53 weeks Flag')
    year_with_53_weeks_iso = models.IntegerField(verbose_name='Year with 53 weeks Flag - ISO')
    is_project_holiday_usa = models.IntegerField(verbose_name='Project Holiday Flag in the USA')
    is_project_holiday_canada = models.IntegerField(verbose_name='Project Holiday Flag in Canada')
    year_week_no_format = models.CharField(max_length=8, verbose_name='Year-Week_No Format')
    year_month_no_week_no_format = models.CharField(max_length=12, verbose_name='Year-Month_no-Week_No Format')
    year_month_no_format = models.CharField(max_length=8, verbose_name='Year-Month_no Format')
    date_year = models.CharField(max_length=4, verbose_name='Year - Text')
    date_quarter_text = models.CharField(max_length=2, verbose_name='Quarter of the Year - Text')
    quarter_title = models.CharField(max_length=4, verbose_name='Quarter Title')
    date_year_quarter_title = models.CharField(max_length=9, verbose_name='Quarter Title of the Year')
    mon_start_date = models.DateTimeField(blank=True, null=True, verbose_name='Mon Start Date')
    sun_finish_date = models.DateTimeField(blank=True, null=True, verbose_name='Sun Finish Date')
    date_range_mon_to_sun = models.CharField(max_length=24, blank=True, null=True, verbose_name='Date Range from Mon to Sun')
    tue_start_date = models.DateTimeField(blank=True, null=True, verbose_name='Tue Start Date')
    mon_finish_date = models.DateTimeField(blank=True, null=True, verbose_name='Mon Finish Date')
    date_range_tue_to_mon = models.CharField(max_length=24, blank=True, null=True, verbose_name='Date Range from Tue to Mon')
    wed_start_date = models.DateTimeField(blank=True, null=True, verbose_name='Wed Start Date')
    tue_finish_date = models.DateTimeField(blank=True, null=True, verbose_name='Tue Finish Date')
    date_range_wed_to_tue = models.CharField(max_length=24, blank=True, null=True, verbose_name='Date Range from Wed to Tue')
    thu_start_date = models.DateTimeField(blank=True, null=True, verbose_name='Thu Start Date')
    wed_finish_date = models.DateTimeField(blank=True, null=True, verbose_name='Wed Finish Date')
    date_range_thu_to_wed = models.CharField(max_length=24, blank=True, null=True, verbose_name='Date Range from Thu to Wed')
    fri_start_date = models.DateTimeField(blank=True, null=True, verbose_name='Fri Start Date')
    thu_finish_date = models.DateTimeField(blank=True, null=True, verbose_name='Thu Finish Date')
    date_range_fri_to_thu = models.CharField(max_length=24, blank=True, null=True, verbose_name='Date Range from Fri to Thu')
    sat_start_date = models.DateTimeField(blank=True, null=True, verbose_name='Sat Start Date')
    fri_finish_date = models.DateTimeField(blank=True, null=True, verbose_name='Fri Finish Date')
    date_range_sat_to_fri = models.CharField(max_length=24, blank=True, null=True, verbose_name='Date Range from Sat to Fri')
    sun_start_date = models.DateTimeField(blank=True, null=True, verbose_name='Sun Start Date')
    sat_finish_date = models.DateTimeField(blank=True, null=True, verbose_name='Sat Finish Date')
    date_range_sun_to_sat = models.CharField(max_length=24, blank=True, null=True, verbose_name='Date Range from Sun to Sat')
# --
    three_months_ago_date = models.DateTimeField(blank=True, null=True, verbose_name='3 months ago - Date')
    three_months_ago_title = models.CharField(max_length=8, blank=True, null=True, verbose_name='3 months ago - Date Title')
    two_months_ago_date = models.DateTimeField(blank=True, null=True, verbose_name='2 months ago - Date')
    two_months_ago_title = models.CharField(max_length=8, blank=True, null=True, verbose_name='2 months ago - Date Title')
    one_months_ago_date = models.DateTimeField(blank=True, null=True, verbose_name='1 months ago - Date')
    one_months_ago_title = models.CharField(max_length=8, blank=True, null=True, verbose_name='1 months ago - Date Title')
# --
    three_weeks_ago_date = models.DateTimeField(blank=True, null=True, verbose_name='3 weeks ago - Date')
    three_weeks_ago_title = models.CharField(max_length=12, blank=True, null=True, verbose_name='3 weeks ago - Date Title')
    two_weeks_ago_date = models.DateTimeField(blank=True, null=True, verbose_name='2 weeks ago - Date')
    two_weeks_ago_title = models.CharField(max_length=12, blank=True, null=True, verbose_name='2 weeks ago - Date Title')
    one_weeks_ago_date = models.DateTimeField(blank=True, null=True, verbose_name='1 weeks ago - Date')
    one_weeks_ago_title = models.CharField(max_length=12, blank=True, null=True, verbose_name='1 weeks ago - Date Title')
# --
    ten_days_ago_date = models.DateTimeField(blank=True, null=True, verbose_name='10 days ago - Date')
    six_days_ago_date = models.DateTimeField(blank=True, null=True, verbose_name='6 days ago - Date')
    five_days_ago_date = models.DateTimeField(blank=True, null=True, verbose_name='5 days ago - Date')
    four_days_ago_date = models.DateTimeField(blank=True, null=True, verbose_name='4 days ago - Date')
    three_days_ago_date = models.DateTimeField(blank=True, null=True, verbose_name='3 days ago - Date')
    two_days_ago_date = models.DateTimeField(blank=True, null=True, verbose_name='2 days ago - Date')
    one_days_ago_date = models.DateTimeField(blank=True, null=True, verbose_name='1 days ago - Date')
# --
    todays_date = models.DateTimeField(blank=True, null=True, verbose_name='Todays Date')
    one_days_hence_date = models.DateTimeField(blank=True, null=True, verbose_name='1 days hence - Date')
    two_days_hence_date = models.DateTimeField(blank=True, null=True, verbose_name='2 days hence - Date')
    three_days_hence_date = models.DateTimeField(blank=True, null=True, verbose_name='3 days hence - Date')
    four_days_hence_date = models.DateTimeField(blank=True, null=True, verbose_name='4 days hence - Date')
    five_days_hence_date = models.DateTimeField(blank=True, null=True, verbose_name='5 days hence - Date')
    six_days_hence_date = models.DateTimeField(blank=True, null=True, verbose_name='6 days hence - Date')
    ten_days_hence_date = models.DateTimeField(blank=True, null=True, verbose_name='10 days hence - Date')
# --
    one_weeks_hence_date = models.DateTimeField(blank=True, null=True, verbose_name='1 weeks hence - Date')
    one_weeks_hence_title = models.CharField(max_length=12, blank=True, null=True, verbose_name='1 weeks hence - Date Title')
    two_weeks_hence_date = models.DateTimeField(blank=True, null=True, verbose_name='2 weeks hence - Date')
    two_weeks_hence_title = models.CharField(max_length=12, blank=True, null=True, verbose_name='2 weeks hence - Date Title')
    three_weeks_hence_date = models.DateTimeField(blank=True, null=True, verbose_name='3 weeks hence - Date')
    three_weeks_hence_title = models.CharField(max_length=12, blank=True, null=True, verbose_name='3 weeks hence - Date Title')
# --
    one_months_hence_date = models.DateTimeField(blank=True, null=True, verbose_name='1 months hence - Date')
    one_months_hence_title = models.CharField(max_length=8, blank=True, null=True, verbose_name='1 months hence - Date Title')
    two_months_hence_date = models.DateTimeField(blank=True, null=True, verbose_name='2 months hence - Date')
    two_months_hence_title = models.CharField(max_length=8, blank=True, null=True, verbose_name='2 months hence - Date Title')
    three_months_hence_date = models.DateTimeField(blank=True, null=True, verbose_name='3 months hence - Date')
    three_months_hence_title = models.CharField(max_length=8, blank=True, null=True, verbose_name='3 months hence - Date Title')

    class Meta:
        managed = True
        verbose_name_plural = 'CAMEOSE Dates'
        db_table = 'dates_cameose'
        app_label = 'c_project_calendar'
        ordering = ['date_code']

    def __str__(self):
        return str('%s' % self.date_code)


# This table is a subset of the dates_cameose table and will only contain dates specific to the project date range
class ProjectCalendar(models.Model):
    date_code = models.CharField(unique=True, max_length=10, verbose_name='Date Code')
    sole_date = models.DateTimeField(unique=True, verbose_name='Date')
    day_no = models.IntegerField(verbose_name='Day Number of the Month')
    day_no_text = models.CharField(max_length=2, verbose_name='Day Number of the Month - Text')
    day_suffix= models.CharField(max_length=2, verbose_name='Day Suffix for Day Number of the Month')
    day_name_short = models.CharField(max_length=3, verbose_name='Day Name - Short')
    day_name_long = models.CharField(max_length=9, verbose_name='Day Name - Long')
    day_no_of_the_week = models.IntegerField(verbose_name='Day Number of the Week')
    day_no_of_the_week_text = models.CharField(max_length=2, verbose_name='Day Number of the Week - Text')
    day_no_of_the_week_in_month = models.IntegerField(verbose_name='Day Number of the Week in the Month')
    day_no_of_the_week_in_month_text = models.CharField(max_length=2,
                                                        verbose_name='Day Number of the Week in the Month - Text')
    day_no_of_the_year = models.IntegerField(verbose_name='Day Number of the Year')
    day_no_of_the_year_text = models.CharField(max_length=2, verbose_name='Day Number of the Year - Text')
    week_no_of_the_year = models.IntegerField(verbose_name='Week Number of the Year')
    week_no_of_the_year_text = models.CharField(max_length=2, verbose_name='Week Number of the Year - Text')
    week_no_of_the_year_iso = models.IntegerField(verbose_name='Week Number of the Year - ISO')
    week_no_of_the_year_iso_text = models.CharField(max_length=2, verbose_name='Week Number of the Year - ISO - Text')
    week_no_of_the_month = models.IntegerField(verbose_name='Week Number of the Month')
    week_no_of_the_month_text = models.CharField(max_length=2, verbose_name='Week Number of the Month - Text')
    first_date_of_the_week = models.DateTimeField(verbose_name='First Date of the Week')
    last_date_of_the_week = models.DateTimeField(verbose_name='Last Date of the Week')
    month_no = models.IntegerField(verbose_name='Month Number of the Year')
    month_no_text = models.CharField(max_length=2, verbose_name='Month Number of the Year - Text')
    month_name_short = models.CharField(max_length=3, verbose_name='Month Name - Short')
    month_name_long = models.CharField(max_length=9, verbose_name='Month Name - Long')
    is_stat_holiday_usa = models.IntegerField(verbose_name='Statutory Holiday Flag in the USA')
    stat_holiday_name_usa = models.CharField(max_length=55, blank=True, null=True, verbose_name='Statutory Holiday Name in the USA')
    is_stat_holiday_canada = models.IntegerField(verbose_name='Statutory Holiday Flag in Canada')
    stat_holiday_name_canada = models.CharField(max_length=55, blank=True, null=True, verbose_name='Statutory Holiday Name in Canada')
    is_weekend = models.IntegerField(verbose_name='Weekend Flag')
    is_leap_year = models.IntegerField(verbose_name='Leap Year Flag')
    year_with_53_weeks = models.IntegerField(verbose_name='Year with 53 weeks Flag')
    year_with_53_weeks_iso = models.IntegerField(verbose_name='Year with 53 weeks Flag - ISO')
    is_project_holiday_usa = models.IntegerField(verbose_name='Project Holiday Flag in the USA')
    is_project_holiday_canada = models.IntegerField(verbose_name='Project Holiday Flag in Canada')
    year_week_no_format = models.CharField(max_length=8, verbose_name='Year-Week_No Format')
    year_month_no_week_no_format = models.CharField(max_length=12, verbose_name='Year-Month_no-Week_No Format')
    year_month_no_format = models.CharField(max_length=8, verbose_name='Year-Month_no Format')
    date_year = models.CharField(max_length=4, verbose_name='Year - Text')
    date_quarter_text = models.CharField(max_length=2, verbose_name='Quarter of the Year - Text')
    quarter_title = models.CharField(max_length=4, verbose_name='Quarter Title')
    date_year_quarter_title = models.CharField(max_length=9, verbose_name='Quarter Title of the Year')
    mon_start_date = models.DateTimeField(blank=True, null=True, verbose_name='Mon Start Date')
    sun_finish_date = models.DateTimeField(blank=True, null=True, verbose_name='Sun Finish Date')
    date_range_mon_to_sun = models.CharField(max_length=24, blank=True, null=True, verbose_name='Date Range from Mon to Sun')
    tue_start_date = models.DateTimeField(blank=True, null=True, verbose_name='Tue Start Date')
    mon_finish_date = models.DateTimeField(blank=True, null=True, verbose_name='Mon Finish Date')
    date_range_tue_to_mon = models.CharField(max_length=24, blank=True, null=True, verbose_name='Date Range from Tue to Mon')
    wed_start_date = models.DateTimeField(blank=True, null=True, verbose_name='Wed Start Date')
    tue_finish_date = models.DateTimeField(blank=True, null=True, verbose_name='Tue Finish Date')
    date_range_wed_to_tue = models.CharField(max_length=24, blank=True, null=True, verbose_name='Date Range from Wed to Tue')
    thu_start_date = models.DateTimeField(blank=True, null=True, verbose_name='Thu Start Date')
    wed_finish_date = models.DateTimeField(blank=True, null=True, verbose_name='Wed Finish Date')
    date_range_thu_to_wed = models.CharField(max_length=24, blank=True, null=True, verbose_name='Date Range from Thu to Wed')
    fri_start_date = models.DateTimeField(blank=True, null=True, verbose_name='Fri Start Date')
    thu_finish_date = models.DateTimeField(blank=True, null=True, verbose_name='Thu Finish Date')
    date_range_fri_to_thu = models.CharField(max_length=24, blank=True, null=True, verbose_name='Date Range from Fri to Thu')
    sat_start_date = models.DateTimeField(blank=True, null=True, verbose_name='Sat Start Date')
    fri_finish_date = models.DateTimeField(blank=True, null=True, verbose_name='Fri Finish Date')
    date_range_sat_to_fri = models.CharField(max_length=24, blank=True, null=True, verbose_name='Date Range from Sat to Fri')
    sun_start_date = models.DateTimeField(blank=True, null=True, verbose_name='Sun Start Date')
    sat_finish_date = models.DateTimeField(blank=True, null=True, verbose_name='Sat Finish Date')
    date_range_sun_to_sat = models.CharField(max_length=24, blank=True, null=True, verbose_name='Date Range from Sun to Sat')
# --
    three_months_ago_date = models.DateTimeField(blank=True, null=True, verbose_name='3 months ago - Date')
    three_months_ago_title = models.CharField(max_length=8, blank=True, null=True, verbose_name='3 months ago - Date Title')
    two_months_ago_date = models.DateTimeField(blank=True, null=True, verbose_name='2 months ago - Date')
    two_months_ago_title = models.CharField(max_length=8, blank=True, null=True, verbose_name='2 months ago - Date Title')
    one_months_ago_date = models.DateTimeField(blank=True, null=True, verbose_name='1 months ago - Date')
    one_months_ago_title = models.CharField(max_length=8, blank=True, null=True, verbose_name='1 months ago - Date Title')
# --
    three_weeks_ago_date = models.DateTimeField(blank=True, null=True, verbose_name='3 weeks ago - Date')
    three_weeks_ago_title = models.CharField(max_length=12, blank=True, null=True, verbose_name='3 weeks ago - Date Title')
    two_weeks_ago_date = models.DateTimeField(blank=True, null=True, verbose_name='2 weeks ago - Date')
    two_weeks_ago_title = models.CharField(max_length=12, blank=True, null=True, verbose_name='2 weeks ago - Date Title')
    one_weeks_ago_date = models.DateTimeField(blank=True, null=True, verbose_name='1 weeks ago - Date')
    one_weeks_ago_title = models.CharField(max_length=12, blank=True, null=True, verbose_name='1 weeks ago - Date Title')
# --
    ten_days_ago_date = models.DateTimeField(blank=True, null=True, verbose_name='10 days ago - Date')
    six_days_ago_date = models.DateTimeField(blank=True, null=True, verbose_name='6 days ago - Date')
    five_days_ago_date = models.DateTimeField(blank=True, null=True, verbose_name='5 days ago - Date')
    four_days_ago_date = models.DateTimeField(blank=True, null=True, verbose_name='4 days ago - Date')
    three_days_ago_date = models.DateTimeField(blank=True, null=True, verbose_name='3 days ago - Date')
    two_days_ago_date = models.DateTimeField(blank=True, null=True, verbose_name='2 days ago - Date')
    one_days_ago_date = models.DateTimeField(blank=True, null=True, verbose_name='1 days ago - Date')
# --
    todays_date = models.DateTimeField(blank=True, null=True, verbose_name='Todays Date')
    one_days_hence_date = models.DateTimeField(blank=True, null=True, verbose_name='1 days hence - Date')
    two_days_hence_date = models.DateTimeField(blank=True, null=True, verbose_name='2 days hence - Date')
    three_days_hence_date = models.DateTimeField(blank=True, null=True, verbose_name='3 days hence - Date')
    four_days_hence_date = models.DateTimeField(blank=True, null=True, verbose_name='4 days hence - Date')
    five_days_hence_date = models.DateTimeField(blank=True, null=True, verbose_name='5 days hence - Date')
    six_days_hence_date = models.DateTimeField(blank=True, null=True, verbose_name='6 days hence - Date')
    ten_days_hence_date = models.DateTimeField(blank=True, null=True, verbose_name='10 days hence - Date')
# --
    one_weeks_hence_date = models.DateTimeField(blank=True, null=True, verbose_name='1 weeks hence - Date')
    one_weeks_hence_title = models.CharField(max_length=12, blank=True, null=True, verbose_name='1 weeks hence - Date Title')
    two_weeks_hence_date = models.DateTimeField(blank=True, null=True, verbose_name='2 weeks hence - Date')
    two_weeks_hence_title = models.CharField(max_length=12, blank=True, null=True, verbose_name='2 weeks hence - Date Title')
    three_weeks_hence_date = models.DateTimeField(blank=True, null=True, verbose_name='3 weeks hence - Date')
    three_weeks_hence_title = models.CharField(max_length=12, blank=True, null=True, verbose_name='3 weeks hence - Date Title')
# --
    one_months_hence_date = models.DateTimeField(blank=True, null=True, verbose_name='1 months hence - Date')
    one_months_hence_title = models.CharField(max_length=8, blank=True, null=True, verbose_name='1 months hence - Date Title')
    two_months_hence_date = models.DateTimeField(blank=True, null=True, verbose_name='2 months hence - Date')
    two_months_hence_title = models.CharField(max_length=8, blank=True, null=True, verbose_name='2 months hence - Date Title')
    three_months_hence_date = models.DateTimeField(blank=True, null=True, verbose_name='3 months hence - Date')
    three_months_hence_title = models.CharField(max_length=8, blank=True, null=True, verbose_name='3 months hence - Date Title')

    class Meta:
        managed = True
        verbose_name_plural = 'Project Calendar'
        db_table = 'project_calendar'
        app_label = 'c_project_calendar'
        ordering = ['date_code']

    def __str__(self):
        return str('%s' % self.date_code)