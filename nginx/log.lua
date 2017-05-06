-- a module to output access log by lua
local LOG_FILE = "/usr/local/openresty/nginx/lua/1.log";
local LOG_FORMAT = 
'$remote_addr - $remote_user [$time_local] "$request" '..
'$status $body_bytes_sent "$http_referer" '..
'"$http_user_agent" "$http_x_forwarded_for"';

--get = ngx.var;

function check(var)
	if(var) then
		return var;
	else
		return "-";
	end
end

function substitute(str)
	return check(ngx.var[str]);
end

function parse_format(format)
	return string.gsub(format, "%$([%w_]+)", substitute);
end

data = parse_format(LOG_FORMAT).."\r\n"
file = io.open(LOG_FILE, "a");
if(file) then
	file:write(data);
	file:close();
end
