select b.title, b.board_id, r.reply_id, r.writer_id, r.contents, date_format(r.created_date,'%Y-%m-%d') as created_date
from used_goods_board as b, used_goods_reply as r
where b.board_id = r.board_id
and b.created_date between date('2022-10-01') and date('2022-10-31')
group by b.board_id
order by r.created_date, b.title;