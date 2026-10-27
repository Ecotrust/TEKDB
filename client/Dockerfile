FROM node:22-bookworm AS builder
WORKDIR /app
COPY . .
RUN npm ci --silent
RUN npm run build

# local development
FROM builder AS dev
WORKDIR /app
EXPOSE 5173
CMD ["npm", "run", "dev", "--", "--host", "0.0.0.0", "--port", "5173", "--strictPort"]