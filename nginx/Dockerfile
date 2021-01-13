# Use the Nginx image
FROM nginx

# Remove the Default nginx.conf
RUN rm /etc/nginx/conf.d/default.conf 

# Replace with Our Own nginx.conf
COPY nginx.conf /etc/nginx/conf.d/
