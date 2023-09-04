-- Table: public.tareas_registrotareas

-- DROP TABLE IF EXISTS public.tareas_registrotareas;

CREATE TABLE IF NOT EXISTS public.tareas_registrotareas
(
    id_tarea character varying(3) COLLATE pg_catalog."default" NOT NULL,
    titulo_tarea character varying(50) COLLATE pg_catalog."default" NOT NULL,
    descripcion_tarea character varying(150) COLLATE pg_catalog."default" NOT NULL,
    fecha_vencimiento_tarea date NOT NULL,
    categoria_tarea character varying(1) COLLATE pg_catalog."default" NOT NULL,
    estado_tarea character varying(1) COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT tareas_registrotareas_pkey PRIMARY KEY (id_tarea)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.tareas_registrotareas
    OWNER to postgres;
-- Index: tareas_registrotareas_id_tarea_0295ce22_like

-- DROP INDEX IF EXISTS public.tareas_registrotareas_id_tarea_0295ce22_like;

CREATE INDEX IF NOT EXISTS tareas_registrotareas_id_tarea_0295ce22_like
    ON public.tareas_registrotareas USING btree
    (id_tarea COLLATE pg_catalog."default" varchar_pattern_ops ASC NULLS LAST)
    TABLESPACE pg_default;
	
select * from public.tareas_registrotareas;